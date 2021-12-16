from time import sleep
import random
'''
 [ opt50007 : 선물시세추이요청 ]
  
 1. Open API 조회 함수 입력값을 설정합니다.
	종목코드 = 전문 조회할 종목코드 ( 101RC000 )
	참조 : https://reviewjang.tistory.com/123
	SetInputValue("종목코드"	,  "입력값 1");

	시간단위 = 00:틱, 1:1분, 5:5분,10:10분,15:15분,30:30분,0:일
	SetInputValue("시간단위"	,  "입력값 2");

	시간검색 = 지원안함 (공백)
	SetInputValue("시간검색"	,  "입력값 3");


 2. Open API 조회 함수를 호출해서 전문을 서버로 전송합니다.
	CommRqData( "RQName"	,  "opt50007"	,  "0"	,  "화면번호"); 

'''
class FuturesLookup:

   def lookup_schedule(self, stock, rising_queue):
       self.stock = stock
       self.rising_queue = rising_queue
       while(True):
           try:
               df = self.stock.block_request("opt50007",
                                    종목코드="101S3000",
                                    시간단위="1",
                                    시간검색="",
                                    output="선물시세추이요청",
                                    next=0)
               self.rising_queue.put(df)
               print("===================================================================================")
           except Exception as e:  # 모든 예외의 에러 메시지를 출력
               print('예외가 발생했습니다.', e)
           finally:
               sleep(random.randrange(3,5))

   def rising_queue(self):
       return self.rising_queue()
