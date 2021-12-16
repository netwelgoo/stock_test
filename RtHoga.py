import Status

class RtHoga:
  def __init__(self, code, time, price, hg201, status):
    self.code = code
    self.hg23 = price  ## 예상 체결가
    self.time = time
    self.hg201 = hg201
    self.status = status

  def __str__(self):
      return 'hoga : code , time , price , hg201 , status '\
                .format(self.code, self.time, self.hg23, self.hg201, self.status)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(RtHoga('종목코드', '120210', '3만원', '2.9만원', Status.Status.WAIT))
