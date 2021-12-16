from datetime import datetime, timezone
import RtHoga, Status

THREE_MIN_SEC = 180
TEN_MIN_SEC   = 600
THREE_PER     = 3
ONE_PER       = 1

class RealTimeHogaAnalisys:
    def __init__(self, order_queue, realtime_hoga):
        self.code = realtime_hoga.t01      ## 종목 코드
        self.order_queue = order_queue      ## 주문 Queue
        self.rt_hoga = realtime_hoga        ## 실시간 호가
        # self.last_rt_hoga_time = datetime.strptime(realtime_hoga.time, '%H%M%S').time() ## 최신 호가 시간
        self.time_hogas = {}                ## 시간,호가(등락률) 정보
        self.max_time_hoga = {}             ## 가장 높은 호가의 시간,호가 정보
        self.min_time_hoga = {}             ## 가장 낮은 호가의 시간,호가 정보
        self.times = []                     ## 실시간 호가의 시간 리스트 정보   //보관 주기 Key 저장
        # self.max_time_hoga[realtime_hoga.time] = realtime_hoga.hg23
        # self.time_hogas[realtime_hoga.time] = realtime_hoga.hg23

# 등락율이 일정 percent 이상
    def closing_price_over_xper(self, now_rate):
        return now_rate > THREE_PER

# 등락율이 1% 이하이면 판다.
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
        if rtHoga.status == Status.Status.BUY :
            return True
        else:
            return False

    def analysis(self, rt_hoga):  ## 실시간 분석
        print('code = ', rt_hoga.t01)
        self.order_queue.put(rt_hoga)
        # self.last_rt_hoga_time = datetime.strptime(rt_hoga.time, '%H%M%S').time()
        # self.times.append(rt_hoga.time)
        # self.time_hogas[rt_hoga.time] = rt_hoga.hg23

## 사야할 조건일 경우
##      if notBuyStatus(rt_hoga) and conditionsToBuy(rt_hoga):

## 팔아야할 조건일 경우
##      if buyStatus(rt_hoga) and conditionsToSell(rt_hoga):

#         ## 제일 높은 호가를 가져온다.
#         if(len(self.max_time_hoga) > 0) :
#             max_hoga = max(self.max_time_hoga.values())
#         if rt_hoga.hg23 > max_hoga :
#             self.max_time_hoga[realtime_hoga.time] = realtime_hoga.hg23
#             print('max price='.format(realtime_hoga.hg23))
#         ## 어제 동시호가 대비 등락율이 3% 이상이고 사지 않은 상태이면 산다.
#             if self.closing_price_over_xper(rt_hoga.hg201) and notBuyStatus(rt_hoga):
#                 rt_hoga.status = Status.Status.REQ_BUY
#                 self.order_queue.put(rt_hoga)
#
#         ## 제일 낮은 호가를 가져온다.
#         if (len(self.min_time_hoga) > 0):
#             min_hoga = max(self.min_time_hoga.values())
#         ## 어제 종가 대비 등락율이 1% 이하이고 구입한 상태이면 판다.
#         if self.closing_price_under_one_per(rt_hoga.hg201) and buyStatus(rt_hoga):
#             rt_hoga.status = Status.Status.REQ_SELL
#             self.order_queue.put(rt_hoga)
#
#         today = datetime.today()
#         ## 10분 이상 지난 데이터는 삭제 한다. (1번)
# #       self.time_hogas = {key: value for key, value in self.time_hogas.items()
# #                          if (datetime.now() - datetime.combine(today, datetime.strptime(key, '%H%M%S').time())).seconds < 600 }
#
#         ## 10분 이상 지난 데이터는 삭제 한다. (2번 - 성능)
#         now_datetime = datetime.now()
#         for time in self.times[:]:
#             if (now_datetime - datetime.combine(today, datetime.strptime(time, '%H%M%S').time())).seconds > 600 :
#                 del self.time_hogas[time]
#                 self.times.remove(time)
#             else:
#                 break
