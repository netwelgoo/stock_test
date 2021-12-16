from FuturesQuote import FuturesQuote
import Status
from datetime import datetime, timezone

class FuturesQuoteAnalyst:
   DISPLAY_SIZE = 30

   def __init__(self, stock):
       self.stock = stock

   def analyze(self, rising_queue):
       print("선물 시세 Queue Display ")
       self.rising_queue = rising_queue
       while(True):
           try:
               futures_quote = self.rising_queue.get()
               futures_quotes = [(FuturesQuote(r.체결시간,  r.시가n , r.고가n , r.저가n , r.현재가n , r.대비기호n , r.전일대비n , r.체결량 , r.누적거래량n , r.미결제약정
                                             ,r.미결제증감 , r.시장베이시스 ,  r.코스피200 , r.종목명 , r.내재가치n
                                             , Status.Status.WAIT, datetime.now()))
                            for index, r in futures_quote.iterrows()]

               for quote in futures_quotes:
                   print(quote)

           except Exception as e:  # 모든 예외의 에러 메시지를 출력
               print('예외가 발생했습니다.', e)
