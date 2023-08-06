#!/usr/bin/env python3

import asyncio
import websockets
import json
import zlib
import time
import requests
import dateutil.parser as dp
import base64
import hmac
import threading
import re

import logging
                
import traceback

from .sdk.spot_api import SpotAPI

from ...common.timer import Timer

from ...base_individual_ws import BaseIndividualWs

from ...events import IndividualOrderEvent,IndividualBalanceEvent,EventType

from ...thread_pool import executor

from .helper import rslv_order_type, rslv_order_status, rslv_symbol

OKEX_URL = 'wss://real.okex.com:10442/ws/v3'



logger = logging.getLogger(__name__) 


def inflate(data):
    decompress = zlib.decompressobj(
            -zlib.MAX_WBITS  # see above
    )
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated


def get_server_time():
    url = "http://www.okex.com/api/general/v3/time"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['iso']
    else:
        return ""

def server_timestamp():
    server_time = get_server_time()
    parsed_t = dp.parse(server_time)
    timestamp = parsed_t.timestamp()
    return timestamp

def login_params(timestamp, api_key, passphrase, secret_key):
    message = timestamp + 'GET' + '/users/self/verify'
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    sign = base64.b64encode(d)

    login_param = {"op": "login", "args": [api_key, passphrase, timestamp, sign.decode("utf-8")]}
    login_str = json.dumps(login_param)
    return login_str


class IndividualWs(BaseIndividualWs):
    """docstring for OkexAdapter"""

    def __init__(self,apikey, secrets,symbols , coins ,listener):
        super(IndividualWs, self).__init__('okex',symbols,secrets,listener)
        
        self._coins = coins

        self.apikey = apikey
        self.secretkey = secrets.get('keysecret')
        self.passphrase = secrets.get('passphrase')

        self.test_balance = False
        self.test_order = False

        self.rest = SpotAPI(self.apikey,self.secretkey,self.passphrase,True)

        self.balance_called = False
        self.order_called = False

    # def rest_coin(self,coin ):

    #     logger.info('get_coin_account_info: %s' , coin.upper())
    #     item = self.rest.get_coin_account_info(coin.upper())

    #     logger.info('coin balance: %s' ,item)
    #     balance = {
    #         "balance":float(item.get('balance')),
    #         "available":float(item.get('available')),
    #         "freeze":float(item.get('frozen'))
    #     }

    #     self._listener.on_balance_update(coin,balance.get('balance'),balance.get('available')
    #         ,balance.get('freeze'))


    def convert_order(self,origin):
    
        detail = {}

        detail['order_id'] = str(origin.get('order_id'))
        detail['coid'] = str(origin.get('client_oid'))
        detail['price'] = str(origin.get('price'))
        detail['size'] = str(origin.get('size'))
        detail['side'] = origin.get('side')
        detail['type'] = rslv_order_type(origin.get('type'),origin.get('order_type')).value
        detail['status'] = rslv_order_status(origin.get('state')).value
        detail['coin'],detail['currency'] = rslv_symbol(origin.get('instrument_id'))
        detail['filled_size'] = origin.get('filled_size')
        detail['filled_notional'] = origin.get('filled_notional')
        detail['timestamp'] = origin.get('timestamp')

        return detail


    def rest_balance(self):

        # self.balance_called = True

        account_info = None

        while not account_info:
            try:
                account_info = self.rest.get_account_info()
            except Exception as e:

                logger.error(traceback.format_exc())
                
        # logger.info(f"account_info,{account_info}")

        items =  account_info 

        balances = {}
        for item in items:
            balances[item.get('currency').lower()] = {
                "balance":float(item.get('balance')),
                "available":float(item.get('available')),
                "freeze":float(item.get('frozen'))
            }

        event = IndividualBalanceEvent('balance',balances, self._exchange, self.apikey , EventType.snapshot )
        self._listener.on_individual_event(event)

        # self._listener.on_balance_snapshot(balances)

    # def rest_order(self):

    #     self.order_called = True

    #     for symbol in self._symbols:
    #         instrument_id = f"{symbol[0].upper()}-{symbol[1].upper()}"

    #         pending_orders = self.rest.get_orders_pending( 0, None, 100,instrument_id)

    #         # logger.info(f"pending_orders,{pending_orders}")

    #         items =  pending_orders 


    #         for items in pending_orders:

    #             if isinstance(items ,dict):
    #                 continue
                
    #             orders = {}
            
    #             for item in items:

    #                 orders[item.get('order_id')] = {
    #                     "order_id": item.get('order_id') ,
    #                     "filled_size":float(item.get('filled_size')),
    #                     "price":float(item.get('price')),
    #                     "size":float(item.get('size')),
    #                     "side":item.get('side'),
    #                     "type":item.get('type'),
    #                     "status":item.get('status')
    #                 }

    #             self._listener.on_order_snapshot(symbol[0],symbol[1],orders)
    def rest_orders(self,coin,currency):



        instrument_id = f"{coin.upper()}-{currency.upper()}"

        orders_all = None
        while not orders_all:
            try:
                orders_all = self.rest.get_orders_list( 'all',instrument_id)
            except Exception as e:
                logger.error(traceback.format_exc())

        for items in orders_all:

            if isinstance(items ,dict):
                continue
            
            # orders = {}
        
            # for item in items:

            #     orders[item.get('order_id')] = {
            #         "order_id": item.get('order_id') ,
            #         "filled_size":float(item.get('filled_size')),
            #         "price":float(item.get('price')),
            #         "size":float(item.get('size')),
            #         "side":item.get('side'),
            #         "type":item.get('type'),
            #         "status":item.get('status')
            #     }


            snapshots = {}

            for item in items:
                snapshots[item.get('order_id')] = item

            # self._listener.on_order_snapshot(coin,currency,orders)
            
            event = IndividualOrderEvent('order',snapshots,self._exchange,self.apikey,coin,currency,EventType.snapshot)

            self._listener.on_individual_event(event)

    def rest_ledger(self, coin,currency,order_id=None):

        instrument_id = f"{coin.upper()}-{currency.upper()}"

        logger.debug('rest_ledger: %s' , instrument_id)

        ledgers_all = None
        while not ledgers_all:
            try:
                ledgers_all = self.rest.get_fills(order_id, instrument_id,None,None,None)
            except Exception as e:
                logger.error(traceback.format_exc())

            
        for items in ledgers_all:

            if isinstance(items ,dict):
                continue

            else:
                return items

    def update_ledger(self,event):

        try:

            logger.debug('will update ledger, %s' , json.dumps( event.message) )

            coin = event.coin
            currency = event.currency
            update = event.message

            time.sleep(3)

            for k,v in update.items():

                order_id = k 

                ledgers = self.rest_ledger(coin,currency,order_id)

                coin_fee = 0
                currency_fee = 0

                for ledger in ledgers:

                    if '0' != ledger.get('fee'):
                        side = ledger.get('side')
                        fee = float(ledger.get('fee'))

                        if 'sell' == side:
                            currency_fee += fee
                        elif 'buy' == side:
                            coin_fee += fee

                if coin_fee or currency_fee:

                    v['coin_fee'] = coin_fee
                    v['currency_fee'] = currency_fee

                    event = IndividualOrderEvent('order',{order_id:v}
                        ,self._exchange, self.apikey ,coin,currency,EventType.update )

                    logger.debug('update ledger: %s', json.dumps(event.message))

                    self._listener.on_individual_event(event)
        except Exception as e:
            logger.error(str(e))


    # subscribe channel need login  
    async def connect(self):

        channels = []

        # spot/account
        for coin in self._coins:

            channel = f"spot/account:{coin.upper()}" 
            channels.append(channel)

        # spot/order
        for symbol_arr in self._symbols:
            
            channel = f"spot/order:{symbol_arr[0].upper()}-{symbol_arr[1].upper()}"

            channels.append(channel)

        logger.info('channels: %s', channels)



        logger.info(f"okex,will connect to:{OKEX_URL}")

        async with websockets.connect(OKEX_URL) as websocket:
        
            self._listener.on_start()

            subscribe_coins = json.loads(json.dumps(self._coins))

            try:

                # login
                timestamp = str(server_timestamp())
                login_str = login_params(str(timestamp), self.apikey, self.passphrase, self.secretkey)
                
                await websocket.send(login_str)
                self._listener.on_sent('<login str,hide content for security>')


                logger.debug(f"sent:{login_str}")


                login_res = await websocket.recv()

                sub_param = {"op": "subscribe", "args": channels}
                sub_str = json.dumps(sub_param)
                await  websocket.send(sub_str)
                self._listener.on_sent(sub_str)
                
                logger.debug(f"sent:{sub_str}")
                

                async def ping():
                    await websocket.send("ping")
                    self._listener.on_sent('ping')
                
                timer = Timer.interval(ping,10,10)

                
                while True:
                    # logger.debug("receive:")

                    res = await websocket.recv()
                    
                    timer.refresh()

                    res = inflate(res)
                    self._listener.on_recv(res)
                    # logger.debug(f"{res}")

                    plain = res.decode('utf-8')

                    logger.debug(f"recv:{plain}")

                    if plain == 'pong':
                        continue

                    obj = json.loads(plain)

                    event  = obj.get('event')
                    table  = obj.get('table')
                    data   = obj.get('data')
                    channel= obj.get('channel')

                    if event == 'subscribe':

                        logger.info(f"subscribe:{plain}")

                        d_order   = re.match( r'spot/order:(.*?)-(.*)' ,channel)
                        if d_order:
                            coin    = d_order.group(1).lower()
                            currency= d_order.group(2).lower()

                            self.rest_orders(coin,currency)
                        d_account = re.match( r'spot/account:(.*)' , channel) 
                        if d_account:

                            coin    = d_account.group(1).lower()
                                
                            subscribe_coins.remove(coin)

                            if len(subscribe_coins) == 0:

                                self.rest_balance()
                            

                        # if not self.order_called:
                        #     threading.Thread(target=self.rest_order).start()

                    if table == 'spot/account':

                        updates = {}

                        for item in data:
                            coin = item.get('currency').lower()  

                            balance = item.get('balance')
                            available = item.get('available')
                            freeze = item.get('hold')

                            updates[coin] = item

                            # self._listener.on_balance_update (coin,balance,available,freeze )

                        event = IndividualBalanceEvent('balance' ,updates, self._exchange, self.apikey ,EventType.update )
                        self._listener.on_individual_event(event)

                        if self.test_balance:
                            break

                     
                    elif table == 'spot/order':

                        
                        for item in data:
    
                            updates = {}

                            detail = self.convert_order(item)


                            # orderid = item.get('order_id')
                            # symbol = item.get('instrument_id').lower().split('-') 
                            # price = item.get('price')
                            # amount = item.get('size')
                            # side = item.get('side')
                            # filled_amount = item.get('filled_size')
                            # status = item.get('status')
                            # timestamp = item.get('timestamp')
                            # tradeid = item.get('trade_id')

                            # logger.debug('order update: %s' , item)

                            updates[detail.get('order_id')] = detail

                            # coin = symbol[0]
                            # currency = symbol[1] 

                            coin = detail.get('coin')
                            currency = detail.get('currency')
                            filled_amount = item.get('filled_size')

                            # self._listener.on_order_update(symbol[0],symbol[1], {item.get('order_id'):item})

                            event = IndividualOrderEvent('order',updates,self._exchange, self.apikey ,coin,currency,EventType.update )

                            self._listener.on_individual_event(event)

                            if float(filled_amount) > 0: 
                                print('will submit update_ledger')
                                executor.submit(self.update_ledger,event)

                        
                        if self.test_order:
                            break


            except websockets.ConnectionClosed as e:

                
                self._listener.on_end()

                self.balance_called = False
                self.order_called = False

                logger.warning(str(e))

                raise
            except Exception as e:

                logger.error(str(e))

                raise

    # unsubscribe channels
    async def unsubscribe(url, api_key, passphrase, secret_key, channels):
        async with websockets.connect(url) as websocket:
            timestamp = str(server_timestamp())

            login_str = login_params(str(timestamp), api_key, passphrase, secret_key)

            await websocket.send(login_str)

            greeting = await websocket.recv()
            # print(f"receive < {greeting}")

            sub_param = {"op": "unsubscribe", "args": channels}
            sub_str = json.dumps(sub_param)
            await  websocket.send(sub_str)
            
            res = await websocket.recv()
            res = inflate(res)
            




if __name__ == '__main__':
    pass












 