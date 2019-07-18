import random, time

word = ['cat','cute','maple','critics']
n = 5
rank = {}

def sortV(x) : #받은 딕셔너리값(,)중 두번째꺼로 정렬
    return x[1]

while True :
    print('1. 문제불러오기 2.타자게임 3.등수 출력 4.저장 5.등수불러오기')
    menu = input('메뉴를 선택하세요\n')
    
    if menu == '1' :
        f = open('basic/test.txt','r',encoding='utf8')
        line = f.readlines()
        for i in line :
            word.append(i.replace('\n',''))
        f.close()

    elif menu == '2' :
        '''input("시작하시려면 엔터를 눌러주세요~!")
        t1 = time.time()
       
        
        while n <= 5 :
            q = random.choice(word)
            print(q)
            inp = input('입력 :')
            if (inp == q) :
                n = n + 1
                print('정답입니다')
            else :               
                print('틀렸습니다!')
        '''
        input("시작하시려면 엔터를 눌러주세요~!")
        t1 = time.time()
        
        ck = 0
        while ck < 5 :    
            q = random.choice(word)
            print(q)
            inp = input('입력 :')
            while q != inp :
                print('틀렸습니다!')
                print(q)
                inp = input('입력 :')
            print('정답입니다')
            ck = ck + 1

        t2 = time.time()
        t = t2 - t1
        name = input("이름을 입력하세요 : ")
        rank[name] = float(t)

        print('총 %.0f초 걸렸습니다'%t) 
    
    elif menu == '3' :
        ranklist = sorted(rank.items(),key=sortV)#rank의 값들로 이루어진 쌍들을 key에 적힌 함수로 넘김
        num = 1
        for k,v in ranklist:
            print('%d등 %s %f초'%(num,k,v))
            num = num+1
    
    elif menu == '4' :
        f = open('rank.txt','w')
        text =''
        items = rank.items()
        for k,v in items :
            text = text + k+ ':' + str(v) +'\n'
        f.writelines(text)
        f.close()        
    
    elif menu == '5' :
        f = open('rank.txt','r')
        line =1
        while line :
            line = f.readline().replace('\n','')
            if not(line=='') :
                k,v=line.split(':')
                rank[k] = float(v)
    else :
        break      