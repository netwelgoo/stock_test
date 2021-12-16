from datetime import datetime, timezone
import multiprocessing as mp
import Status, OrderStock

THREE_MIN_SEC = 180
TEN_MIN_SEC   = 600
THREE_PER     = 3
ONE_PER       = 1

class StockAnalyst:
    order_queue= mp.Queue()

    # 초기화
    # def __init__(self, order_queue, hoga_queue, realtime_hoga):
    #     self.realtime_hoga =realtime_hoga  # 실시간 호가
    #     self.order_queue = order_queue     # 주문 큐
    #     self.hoga_queue = hoga_queue       # 호가 큐(실시간 호가 정보를 받는다)
    #     self.last_rt_hoga_time = datetime.strptime(realtime_hoga.time, '%H%M%S').time() ## 최신 호가 시간
    #     self.time_hogas = {}                ## 시간,호가(등락률) 정보
    #     self.max_time_hoga = {}             ## 가장 높은 호가의 시간,호가 정보
    #     self.min_time_hoga = {}             ## 가장 낮은 호가의 시간,호가 정보
    #     self.times = []                     ## 실시간 호가의 시간 리스트 정보   //보관 주기 Key 저장
    #     self.max_time_hoga[realtime_hoga.time]  = realtime_hoga.r3
    #     self.time_hogas[realtime_hoga.time]     = realtime_hoga.r3

    # 등락율이 일정 3% percent 이상
    def closing_price_over_xper(self, now_rate):
        return now_rate > THREE_PER

    # 등락율이 3% 이하이면 판다.
    def closing_price_under_one_per(self, now_rate):
        return now_rate <= ONE_PER

    # 사지 않은 상태
    def notBuyStatus(self, rtHoga):
        if rtHoga.status == Status.Status.WAIT or rtHoga.status == Status.Status.SELL:
            return True
        else:
            return False

    # 구입한 상태
    def buyStatus(self, rtHoga):
        if rtHoga.status == Status.Status.BUY:
            return True
        else:
            return False

    # 실시간 분석 multiprocessing
    def analysis(self, order_queue, hoga_queue, realtime_hoga):
        self.realtime_hoga = realtime_hoga  # 실시간 호가
        self.order_queue = order_queue  # 주문 큐
        self.hoga_queue = hoga_queue  # 호가 큐(실시간 호가 정보를 받는다)
        # self.last_rt_hoga_time = datetime.strptime(realtime_hoga.time, '%H%M%S').time()  ## 최신 호가 시간
        self.last_rt_hoga_time = realtime_hoga.time  # 호가 시간
        self.time_hogas = {}  ## 시간,호가(등락률) 정보
        self.max_time_hoga = {}  ## 가장 높은 호가의 시간,호가 정보
        self.min_time_hoga = {}  ## 가장 낮은 호가의 시간,호가 정보
        self.times = []  ## 실시간 호가의 시간 리스트 정보   //보관 주기 Key 저장
        self.max_time_hoga[realtime_hoga.time] = realtime_hoga.r3
        self.time_hogas[realtime_hoga.time] = realtime_hoga.r3

        while True:
            try:
                realtime_hoga = hoga_queue.get()
                print(realtime_hoga)
                self.last_rt_hoga_time = realtime_hoga.time

                if(len(self.max_time_hoga) > 0) :
                    max_hoga = max(self.max_time_hoga.values())
                    if(realtime_hoga > max_hoga):
                        self.max_time_hoga[realtime_hoga.time] = realtime_hoga.r3

                order_stock = OrderStock(realtime_hoga.r0,
                                         realtime_hoga.r3,
                                         realtime_hoga.r3+1,
                                         '0',  # 거래 요청 시간
                                         '',
                                         Status.Status.REQ_BUY,
                                         1 )

                order_queue.put(order_stock)
            except:
                print('error 발생함.')

