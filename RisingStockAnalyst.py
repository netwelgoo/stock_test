from RealtimeHoga import RealtimeHoga
import Status
from datetime import datetime, timezone

class RisingStockAnalyst:
   RISING_SIZE = 30

   def __init__(self, stock):
       self.stock = stock

   def analyze(self, rising_queue):
       self.rising_queue = rising_queue
       while(True):
           try:
               rising_stocks = self.rising_queue.get().head(self.RISING_SIZE)
               rising_hogas = [(RealtimeHoga(r.종목코드, r.종목정보, r.종목명, r.현재가,
                                          r.전일대비기호, r.전일대비, r.등락률, r.거래량,
                                          r.전일거래량, r.매도잔량, r.매도호가, r.매수호가,
                                          r.매수잔량, r.횟수, Status.Status.WAIT, datetime.datetime.now()))
                            for index, r in rising_stocks.iterrows()]

               for rising_hoga in rising_hogas:
                   print(rising_hoga)

           except:
               print("")


