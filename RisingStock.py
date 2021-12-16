from time import sleep
import random
'''
[ opt10017 : 상하한가요청 ]

 1. Open API 조회 함수 입력값을 설정합니다.
	시장구분 = 000:전체, 001:코스피, 101:코스닥
	SetInputValue("시장구분"	,  "입력값 1");

	상하한구분 = 1:상한, 2:상승, 3:보합, 4: 하한, 5:하락, 6:전일상한, 7:전일하한
	SetInputValue("상하한구분"	,  "입력값 2");

	정렬구분 = 1:종목코드순, 2:연속횟수순(상위100개), 3:등락률순
	SetInputValue("정렬구분"	,  "입력값 3");

	종목조건 = 0:전체조회,1:관리종목제외, 3:우선주제외, 4:우선주+관리종목제외, 5:증100제외, 6:증100만 보기, 7:증40만 보기, 8:증30만 보기, 9:증20만 보기, 10:우선주+관리종목+환기종목제외
	SetInputValue("종목조건"	,  "입력값 4");

	거래량구분 = 00000:전체조회, 00010:만주이상, 00050:5만주이상, 00100:10만주이상, 00150:15만주이상, 00200:20만주이상, 00300:30만주이상, 00500:50만주이상, 01000:백만주이상
	SetInputValue("거래량구분"	,  "입력값 5");

	신용조건 = 0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체
	SetInputValue("신용조건"	,  "입력값 6");

	매매금구분 = 0:전체조회, 1:1천원미만, 2:1천원~2천원, 3:2천원~3천원, 4:5천원~1만원, 5:1만원이상, 8:1천원이상
	SetInputValue("매매금구분"	,  "입력값 7");


 2. Open API 조회 함수를 호출해서 전문을 서버로 전송합니다.
	CommRqData( "RQName"	,  "opt10017"	,  "0"	,  "화면번호"); 

'''
class RisingStock:
   # def __init__(self):
       # self.stock = stock
       # self.stock.CommConnect(block=True)
       # accno = self.stock.GetLoginInfo("ACCNO")[0]
       # print("MY - 계좌번호=" + accno)

   def rising_stock_schedule(self, stock, rising_queue):
       self.stock = stock
       self.rising_queue = rising_queue
       while(True):
           try:
               df = self.stock.block_request("opt10017",  # [ opt10017 : 상하한가요청 ]
                                    시장구분="001",
                                    상하한구분="2",
                                    정렬구분="3",
                                    종목조건="0",
                                    거래량구분="00000",
                                    신용조건="0",
                                    매매금구분="0",
                                    output="상하한가요청",
                                    next=0)

               print('상한가 요청 data format', format(df.head(30)))
               self.rising_queue.put(df)
           except Exception as e:  # 모든 예외의 에러 메시지를 출력
               print('상한가 요청시 예외가 발생했습니다.', e)
           finally:
               sleep(random.randrange(3,5))

   def rising_queue(self):
       return self.rising_queue()
