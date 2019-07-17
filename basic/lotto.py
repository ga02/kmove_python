import random ##외장함수
list = []
for i in range(0,5) : ##range(5)라고 해도됌
    for j in range(0,6) :##()는 
        n = random.randint(1,45)
        while list.count(n) > 0 :
            n = random.randint(1,45)
        list.append(n)
    list.sort() ##클래스 객체 사용함수
    print('로또 :',list) ##내장함수 사용  
    list.clear() 

print()
for i in range(5) : ##쌤이 하신거
    lotto = [0,0,0,0,0,0]
    for x in range(6) :
        num=0
        while(num in lotto):## 리스트안에 있는지 !!!!
            num = random.randint(1,45)
        lotto[x] = num
    print("로또 :",sorted(lotto))    

    print()
    for i in range(1,6) :
        print("로또 :",sorted(random.sample(range(1,46),6)))    ##sample은 중복된거 안뽑