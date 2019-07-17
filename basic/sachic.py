import random
import time

input("게임을 시작하시려면 엔터를 누르세요~")
t1 = time.time()
count = 0
list = ['+','-','*','//']

for i in range(5) :
    s = random.choice(list)
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)

    quiz = str(num1) + s + str(num2)#quiz ='%d %s %d'%(num1,s,num2)
       
    print(quiz," = ?")
    x = int(input('정답 : '))
    a = int(eval(quiz))
    if(a == x) :
        count = count +1
        print("정답!")
    else :
        print("틀렸습니다. 정답은 %d 입니다"%a)
      
t2 = time.time()
print('\n맞힌 갯수는 %d개 입니다'%count) #복습하기 !!!! 다시 만들어보기 안보고
print("총 %.0f초 걸렸습니다."%(t2-t1))   
 