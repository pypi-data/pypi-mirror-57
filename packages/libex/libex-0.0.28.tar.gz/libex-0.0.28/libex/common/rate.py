import logging
import json
from ..events import EventType,MarketEvent


logger = logging.getLogger(__name__)

class Rate(object):
    """docstring for Rate"""
    def __init__(self,exchange, currencies,stablecoin,listener):
        super(Rate, self).__init__()
        self.exchange = exchange
        self.currencies = currencies
        self.stablecoin = stablecoin
        # self.rates = {}
        self.listener = listener


    def on_ticker(self, coin, currency, timestamp, detail):

        
        key = "%s_%s" % (coin,currency)

        # logger.info('rate ticker: %s' , key)
        # logger.info('currencies: %s, stable: %s' , json.dumps(self.currencies), self.stablecoin)

        # logger.info('coin: %s, currencies: %s, currency: %s, stable: %s',coin,self.currencies,currency,self.stablecoin)
        if coin in self.currencies and currency == self.stablecoin:
            # self.rates[key] = detail.get('last')
            
            rate = detail.get('last')

            # logger.info('rate: %s', rate)
            self.listener.on_market_event( MarketEvent('rate', rate, self.exchange,coin,currency ))

            
