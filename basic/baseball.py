#숫자 자리 일치-스트라이크 / 숫자ㅇ 자리x -볼/ 스트라이크3개 - 멈춤
import random

num = random.sample(range(1,10),3)

count = 0

while True :
    snum = 0
    bnum = 0
    print(num)
    n = list(input("숫자를 입력하세요 : ")) ##!!!!!!
    
    for i in range(3) :        
        for j in range(3) :
            if num[i] == int(n[j]) :
                if i == j :
                    snum = snum +1
                else :
                    bnum = bnum +1
    count = count + 1
    if snum == 3 :
        print("정답입니다. %d번 만에 맞췄습니다."%count)
        break   
    print("스트라이크 : %d   볼 : %d"%(snum,bnum))
    n.clear()
   


# 쌤이 한거
for i in num :
    for j in n :
        if i == int(j) :
            if num.index(i) == n.index(j) :
                print("스트라이크")

