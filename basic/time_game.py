import time

input("시작하시려면 엔터를 누르세요~")
t1 = time.time()
input('20초 후 다시 엔터를 누르세요 !~')
t2 = time.time()
r = t2 - t1
print("%.0f초 지났습니다"%r)
print("차이 : %.0f"%(20-r)) #print("차이 :",abs(et-20),"초") 절댓값으로 출력
 