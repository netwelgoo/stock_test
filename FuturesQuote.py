import Status
from datetime import datetime, timezone

class FuturesQuote:
  def __init__(self, h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, status, time):
      self.r0 = h0              # 체결시간
      self.r1 = h1              # 시가n
      self.r2 = h2              # 고가n
      self.r3 = h3         # 저가n
      self.r4 = h4              # 현재가n
      self.r5 = h5              # 대비기호n
      self.r6 = h6       # 전일대비n
      self.r7 = h7       # 체결량
      self.r8 = h8         # 누적거래량n
      self.r9 = h9         # 미결제약정
      self.r10= h10        # 미결제증감
      self.r11= h11             # 시장베이시스
      self.r12= h12             # 코스피200
      self.r13= h13             # 종목명
      self.r14 = h14            # 내재가치n
      self.status = status
      self.time = time

  def set_status_time(self, status, time):
      self.status = status
      self.time = time

  def set_time(self, time):
      self.time = time

  def set_status(self, status):
      self.status = status

  def __str__(self):
      return '선물 : 체결시간={} ,  시가n={} , 고가n={} , 저가n={} , 현재가n={} , 대비기호n={} , 전일대비n={} , 체결량={} ' \
             ', 누적거래량n={} , 미결제약정={} , 미결제증감={} , 시장베이시스={} ,  코스피200={} , 종목명={} , 내재가치n={}  , 상태={} , 시간={} '\
                .format(self.r0,self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7, self.r8, self.r9, self.r10,self.r11,self.r12,self.r13, self.r14, self.status, self.time)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    futuresQuote = FuturesQuote('t0', 't1',  't2',  't3',  't4',  't5',  't6',  't7',  't8',  't9',  't10', 't11', 't12', 't13', 't14')
    futuresQuote.set_status_time(Status.Status.WAIT, datetime.now())
    print(futuresQuote)
