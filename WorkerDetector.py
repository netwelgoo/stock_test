import threading, queue
import RtHoga, Status, StockAnalyst
import multiprocessing as mp

# def Status(*sequential, **named):
#     enums = dict(zip(sequential, range(len(sequential))), **named)
#     return type('Enum', (), enums)

class WorkerDetector:
   def __init__(self, realtime_queue):
     self.realtime_queue = realtime_queue
     self.order_queue = mp.Queue()
     self.hoga_process_container = {}  # key = code(r0), value = process
     self.realtime_queue_container = {}  # key = code(r0), value = realtime_queue

   # 실시간 호가 정보를 queue에서 가져온다.
   #
   def detect(self):
      while True:
        rt_hoga = self.realtime_queue.get()
        if rt_hoga.r0 not in self.hoga_process_container:
            stock_analyst = StockAnalyst.StockAnalyst()
            realtime_hoga_queue = mp.Queue()
            p = mp.Process(target=stock_analyst.analysis, args=(realtime_hoga_queue, self.order_queue, rt_hoga,))
            p.start()
            self.hoga_process_container[rt_hoga.r0] = p
            self.realtime_queue_container[rt_hoga.r0] = realtime_hoga_queue
        else:
            realtime_hoga_queue = self.realtime_queue_container[rt_hoga.r0]
            realtime_hoga_queue.put(rt_hoga)

   def getOrder_queue(self):
       return self.order_queue

   def realtime_process_size(self):
       return len(self.hoga_process_container)

if __name__ == '__main__':
    all_realtime_queue = queue.Queue()
    worker = WorkerDetector(all_realtime_queue)

    threading.Thread(target=worker.detect, daemon=True).start()
    ##Process(target=worker.detect, daemon=True).start()
               ## 종목코드, 시간(24hhmiss), 현재가, 전일종가대비 등락률, 상태

    status = Status.Status.WAIT
    if worker.hoga_container.has_key('좀목코드'):
        status = worker.hoga_container['종목코드'].status

    rt_hoga = RtHoga.RtHoga('000001', '123451', 1000, 900,  status)

    rt_hoga2 = RtHoga.RtHoga('000001', '123453', 2000, 1900, Status.Status.WAIT)
    rt_hoga3 = RtHoga.RtHoga('000001', '123455', 2000, 1900, Status.Status.WAIT)
    rt_hoga4 = RtHoga.RtHoga('000001', '123457', 2000, 1900, Status.Status.WAIT)
    rt_hoga5 = RtHoga.RtHoga('000001', '123459', 2000, 1900, Status.Status.WAIT)
    rt_hoga6 = RtHoga.RtHoga('000001', '123503', 2000, 1900, Status.Status.WAIT)
    rt_hoga7 = RtHoga.RtHoga('000001', '123507', 2000, 1900, Status.Status.WAIT)

    rt_queue.put(rt_hoga1)
    rt_queue.put(rt_hoga2)

    result = order_queue.get()

    print('result order is ', result.code, result.hg23, result.time)