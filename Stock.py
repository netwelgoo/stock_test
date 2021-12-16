from pykiwoom.kiwoom import *
import threading, queue
import datetime
# from multiprocessing import Process
import FuturesLookup, RisingStock, Status
from FuturesQuoteAnalyst import FuturesQuoteAnalyst
from RealtimeHoga import RealtimeHoga
import multiprocessing as mp
import RisingStockAnalyst
from SendOrder import SendOrder


class Stock(Kiwoom):
    def __init__(self):
        super().__init__()
        self.CommConnect(block=True)
        accno = self.GetLoginInfo("ACCNO")[0]
        print("MY 계좌번호=" + accno)

        print("실시간 데이터 등록 시작 --> ")
        self._set_real_slot()

        # 전체 조건식 리스트 얻기
        super().GetConditionLoad()
        conditions = super().GetConditionNameList()
        print("조건식 = ", conditions)
        # # 0번 조건식에 해당하는 종목 리스트 출력
        # condition_index = conditions[0][0]
        # condition_name = conditions[0][1]
        # codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)
        #
        # print("조건식 리스트 = {}".format(codes))


    def _set_real_slot(self):
#       실시간 이벤트를 받고 싶은 주식코드 정보를 등록한다.
#       self.SetRealReg("2000", "", "215;20;214", 0)
        self.ocx.OnReceiveRealData.connect(self._handler_real_data)

    def _disConnect_onReceiveRealData(self):
        self.DisconnectRealData(self)

    def _handler_real_data(self, code, real_type, data):
        print(code, real_type, data)

        if real_type == "장시작시간":
            gubun = self.GetCommRealData(code, 215)
            remained_time = self.GetCommRealData(code, 214)
            print(gubun, remained_time)

        if real_type == "주식호가잔량":
            hoga_time       = self.GetCommRealData(code, 21)
            ask01_price     = self.GetCommRealData(code, 41)
            ask01_volume    = self.GetCommRealData(code, 61)
            bid01_price     = self.GetCommRealData(code, 51)
            bid01_volume    = self.GetCommRealData(code, 71)
            print(hoga_time)
            print(f"매도호가: {ask01_price} - {ask01_volume}")
            print(f"매수호가: {bid01_price} - {bid01_volume}")

            ask02_price = self.GetCommRealData(code, 42)
            ask02_volume = self.GetCommRealData(code, 62)
            bid02_price = self.GetCommRealData(code, 52)
            bid02_volume = self.GetCommRealData(code, 72)
            print("매도호가2" + ask02_price)
            print(f"매도호가: {ask02_price} - {ask02_volume}")
            print(f"매수호가: {bid02_price} - {bid02_volume}")

    def set_real_reg(self, screen_no, code_list, fid_list, real_type):
        self.ocx.dynamicCall("SetRealReg(QString, QString, QString, QString)", screen_no, code_list, fid_list, real_type)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    rising_queue    = mp.Queue()
    order_queue     = mp.Queue()
    stock = Stock()
    # sendOrder = SendOrder()
#    rising_stock_analyst = RisingStockAnalyst.RisingStockAnalyst(stock)
    # rising_stock = RisingStock.RisingStock()

    # rising_stock.rising_stock_schedule(stock, rising_queue)
#    threading.Thread(target=rising_stock_analyst.analyze,   args=(rising_queue, )).start()
#    threading.Thread(target=rising_stock.rising_stock_schedule, args=(stock,rising_queue)).start()

    # 선물 시세 추이 분석
    futures_quote_analyst = FuturesQuoteAnalyst(stock)
    futures_lookup = FuturesLookup.FuturesLookup()
    threading.Thread(target=futures_quote_analyst.analyze, args=(rising_queue,)).start()
    threading.Thread(target=futures_lookup.lookup_schedule, args=(stock,rising_queue)).start()

    #p = mp.Process(target=rising_stock.rising_stock_schedule, args=(stock, rising_queue,))
    #p.start()

    #
    # df = rising_queue.get()
    #
    # realtimeHogas = [(RealtimeHoga(r.종목코드,r.종목정보,r.종목명,r.현재가,
    #                                r.전일대비기호,r.전일대비,r.등락률,r.거래량,
    #                                r.전일거래량,r.매도잔량,r.매도호가,r.매수호가,
    #                                r.매수잔량,r.횟수, Status.Status.WAIT, datetime.datetime.now()))
    #                  for index, r in df.iterrows()]
    #
    # # 분석 / buy/sell
    # realtime_queue = queue.Queue()            # realtime Hoga queue
    # worker = WorkerDetector.WorkerDetector(realtime_queue)
    # threading.Thread(target=worker.detect, daemon=False).start()
    #
    # # Process(target=worker.detect).start()
    # status = Status.Status.WAIT
    #
    # for r in realtimeHogas:
    #     realtime_queue.put(r)
    #     print(r)


    # stock.SetRealReg("7000", "", "215;20;214", 0)
    # stock.SetRealReg("1002", "009900", "41", 1)
    # stock.SetRealReg("1003", "082740", "41", 1)
    # stock.SetRealReg("1004", "001680", "41", 1)
    #
    # stock.DisconnectRealData("7000")
    # stock.DisconnectRealData("1002")
    # stock.DisconnectRealData("1003")
    # stock.DisconnectRealData("1004")

    # 주식 사고 파는 메소드
    # stock.SendOrder("시장가매수", "0101", accno, 1, "005930", 10, 0, "03", "")
    # stock.SendOrder("시장가매도", "0101", accno, 1, "005930", 10, 0, "03", "")
    print("실시간 호출 Starting >> ")
    app.exec_()
    print("======================")


    # while(True):
    #     result = worker.getOrder_queue().get()
    #     print('result order is ', result.t01, result.t02)


