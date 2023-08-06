import json
import logging

from ...events import EventType,MarketEvent

from ...const import Channel


logger = logging.getLogger(__name__)

books = {}
events = {}

BOOK_LENGTHS = [10,20,100,200]

def register_event(event,cb):

    events[event] = cb

def books_snapshot(coin,currency,timestamp,detail):
    logger.debug('books_snapshot, coin:%s ,currency:%s ,timestamp:%s , detail:%s', coin,currency,timestamp,detail)

    key = "%s_%s" % (coin,currency)

    asks = detail.get('asks')
    bids = detail.get('bids')

    books.setdefault(key,{})['asks'] = sorted(asks, key=lambda a: a[0])[0:200]
    books.setdefault(key,{})['bids'] = sorted(bids, key=lambda a: a[0],reverse=True)[0:200]

    for length in BOOK_LENGTHS:

        _touch_book(coin,currency,length)


def books_update(coin,currency,timestamp,detail):

    logger.debug('books_update: %s' , detail)

    asks = detail.get('asks')
    bids = detail.get('bids')


    logger.debug(f"update depth,{coin}_{currency}, asks:{asks} , bids:{bids} , timestamp:{timestamp}\n")

    key = "%s_%s" % (coin,currency)

    prev_books = json.loads(json.dumps(books))

    if asks:
        curr_asks = books.setdefault(key,{}).setdefault('asks',[])
    
        for item in asks:

            arr = [n for n in curr_asks if n[0] != item[0]]

            if item[1] != '0':
                arr.append(item)

            curr_asks = arr

        sorted_asks = sorted(curr_asks, key=lambda a: a[0])[0:200]  # 按每个元素的第一个数据排序
        books.setdefault(key,{})['asks'] = sorted_asks

    if bids:        
        curr_bids = books.setdefault(key,{}).setdefault('bids',[])

        for item in bids: 

            arr = [n for n in curr_bids if n[0] != item[0]]

            if item[1] != '0':
                arr.append(item)

            curr_bids = arr

    
        sorted_bids = sorted(curr_bids, key=lambda a: a[0],reverse=True)[0:200]  # 按每个元素的第一个数据排序
        books.setdefault(key,{})['bids'] = sorted_bids
      
    books.setdefault(key,{})['timestamp'] = timestamp

    for length in BOOK_LENGTHS:

        if _diff_books(prev_books.get(key).get('asks')[:length] ,prev_books.get(key).get('bids')[:length] 
            , books.get(key).get('asks')[:length] ,books.get(key).get('bids')[:length] ):
            
            # _touch_book(coin,currency,length)


            key = "%s_%s" % (coin,currency)

            cb = events.get(Channel(f'book{length}'))

            if cb:

                if length <= 20:

                    detail = {
                        'asks':books.setdefault(key,{})['asks'][0:length],
                        'bids':books.setdefault(key,{})['bids'][0:length]
                    }

                    cb(MarketEvent(f'book{length}',detail ,'okex', coin,currency))
                elif length == 200:

                    detail = {
                        'asks':asks,
                        'bids':bids
                    }                    

                    cb(MarketEvent(f'book{length}',detail ,'okex', coin,currency , EventType.update))

def _diff_books(asks1,bids1,asks2,bids2):

    if len(asks1) != len(asks2) or len(bids1) != len(bids2):
        return True

    for i in range(len(asks1)):

        if (asks1[i][0] != asks2[i][0] or asks1[i][1] != asks2[i][1]):
            return True

    for i in range(len(bids1)):
        if (bids1[i][0] != bids2[i][0] or bids1[i][1] != bids2[i][1]):
            return True

    return False
            
def _touch_book(coin,currency,length):

    logger.debug('touch_book, %s, %s, %s', coin, currency, length)
    logger.debug('events: %s', events)

    key = "%s_%s" % (coin,currency)

    cb = events.get(Channel(f'book{length}'))

    if cb:

        detail = {
            'asks':books.setdefault(key,{})['asks'][0:length],
            'bids':books.setdefault(key,{})['bids'][0:length]
        }

        cb(MarketEvent(f'book{length}',detail ,'okex', coin,currency))
