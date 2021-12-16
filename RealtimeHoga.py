import Status
from datetime import datetime, timezone

class RealtimeHoga:
  def __init__(self, h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, status, time):
      self.r0 = h0         # 종목코드
      self.r1 = h1         # 종목정보
      self.r2 = h2         # 종목명
      self.r3 = int(h3)    # 현재가
      self.r4 = h4         # 전일대비기호
      self.r5 = h5         # 전일대비
      self.r6 = float(h6)         # 등락률
      self.r7 = float(h7)         # 거래량
      self.r8 = int(h8)         # 전일거래량
      self.r9 = int(h9)         # 매도잔량
      self.r10= int(h10)        # 매도호가
      self.r11= int(h11)        # 매수호가
      self.r12= int(h12)        # 매수잔량
      self.r13= int(h13)        # 횟수
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
      return 'hoga : 종목코드 , 종목정보 , 종목명 , 현재가 , 전일대비기호 , 전일대비 , 등락률 , 거래량 , 전일거래량 , 매도잔량 , 매도호가 , 매수호가 , 매수잔량 , 횟수 , 상태 , 시간 '\
                .format(self.r0,self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7, self.r8, self.r9, self.r10,self.r11,self.r12,self.r13, self.status, self.time)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    realtime_hoga = RealtimeHoga('t0', 't1',  't2',  't3',  't4',  't5',  't6',  't7',  't8',  't9',  't10', 't11', 't12', 't13')
    realtime_hoga.set_status_time(Status.Status.WAIT, datetime.now())
    print(realtime_hoga)
