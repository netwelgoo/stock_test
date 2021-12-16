import Status

class OrderStock:

  def __init__(self, code, price, req_money, req_time, res_time, status, market_order):
      self.r0 = code                # 종목코드
      self.r3 = price               # 현재가
      self.req_money = req_money    # 요청가 (Status buy / sell)
      self.req_time = req_time      # 거래 요청 시간
      self.res_time = res_time      # 거래 결과 시간
      self.status = status          # 상태
      self.market_order = market_order # 시장가 여부(True:시장가, False:지정가)
      self.req_count = price/1000000 # 구입 개수

  def __str__(self):
      return 'order : 종목코드 , 현재가 , 요청가 , 거래요청시간 , ' \
             '거래결과시간 , 상태 , 시장가여부 , 요청개수 '\
          .format(self.r0, self.r3, self.req_money, self.req_time, self.res_time, self.status, self.market_order, self.req_count)
