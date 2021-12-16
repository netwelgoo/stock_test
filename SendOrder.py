from pykiwoom import kiwoom
from pykiwoom.kiwoom import *


'''
-- 매수/매도 주문

LONG SendOrder() Prarmeters
sRQName	사용자가 임의로 지정할 수 있는 이름입니다. (예: "삼성전자주문")
sScreenNO	화면번호로 "0"을 제외한 4자리의 문자열을 사용합니다. (예: "1000")
sAccNo	계좌번호입니다. (예: "8123123123")
nOrderType	주문유형입니다. (1: 매수, 2: 매도, 3: 매수취소, 4: 매도취소, 5: 매수정정, 6: 매도 정정)
sCode	매매할 주식의 종목코드입니다.
nQty	주문수량입니다.
nPrice	주문단가입니다.
sHogaGb	'00': 지정가, '03': 시장가
sOrgOrderNo	원주문번호로 주문 정정시 사용합니다.
'''

class SendOrder:
    def __init__(self):
        accounts = kiwoom.GetLoginInfo("ACCNO")
        stock_account = accounts[0]
        print("계좌 정보 = {}".format(stock_account))

    def buy(self, RQName, screenNo, accNo, sCode, nQty, nPrice, sHogaGb, sOrgOrderNo):
        self.order(self, RQName, screenNo, accNo, 1, sCode, nQty, nPrice, sHogaGb, sOrgOrderNo)

    def buy_cancel(self, RQName, screenNo, accNo, sCode, nQty, nPrice, sHogaGb, sOrgOrderNo):
        self.order(self, RQName, screenNo, accNo, 3, sCode, nQty, nPrice, sHogaGb, sOrgOrderNo)

    def sell(self, RQName, screenNo, accNo, sCode, nQty, nPrice, sHogaGb, sOrgOrderNo):
        self.order(self, RQName, screenNo, accNo, 2, sCode, nQty, nPrice, sHogaGb, sOrgOrderNo)

    def sell_cancel(self, RQName, screenNo, accNo, sCode, nQty, nPrice, sHogaGb, sOrgOrderNo):
        self.order(self, RQName, screenNo, accNo, 4, sCode, nQty, nPrice, sHogaGb, sOrgOrderNo)

    def order(self, RQName, screenNo, accNo, orderType, sCode, nQty, nPrice, sHogaGb, sOrgOrderNo):
       kiwoom.SenderOrder(RQName, screenNo, accNo, orderType, sCode, nQty, nPrice, sHogaGb, sOrgOrderNo)
