import re
import pickle
custlist=[]
page=-1

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제  
    S - 정보 저장
    F - 불러오기
    Q - 프로그램 종료
    ''').upper()

    if choice=="I": 
        customer={'name':'','sex':'',"email":'',"birthyear":''}       
        print("고객 정보 입력")
        customer['name'] = input("이름 :")
        while True :
            customer['sex']= input("성별(F or M) :").upper()
            if customer['sex'] in ('F','M') :
                break
        '''while customer['sex'] != 'F' and 'M' :
            customer['sex']= input("성별(W or M) :").upper()'''
        while True :
            regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$')
            while True :
                customer['email'] = input("이메일 :")
                golbang = regex.search(customer['email'])
                if golbang :
                    break
                else :
                    print('"@"를 포함한 정확한 이메일을 써주세요')  

            check = 0
            for i in custlist :
                if i['email'] == customer['email'] :
                    check = 1

            if check == 0:
                break
            print('중복되는 이메일이 있습니다.')                 
        while True :
            customer['birthyear'] = input('출생년도 4자리 :')
            if len(customer['birthyear']) == 4 and customer['birthyear'].isdigit():
                break
        '''customer['birthyear'] = input("생일 :")
        while len(customer['birthyear'])!=4 :
            customer['birthyear'] = input("생일(4글자로 입력해주세요!):")'''
        page = page + 1
        custlist.append(customer)
        print(custlist)   

        #page = len(custlist)-1

    elif choice=="C":
        if page != -1 :
            print("현재 고객 정보 조회")
            info = custlist[page]
            key = list(info.keys())
            value = list(info.values())
            for i in range(len(info)) :
                print("%s : %s"%(key[i],value[i]))
            print('현재 페이지는 {}쪽 입니다'.format(page+1))    
        else :
            print('고객정보가 존재 하지 않습니다')
            print(page)

    elif choice == 'P':
        if page-1 != -1 :
            print("이전 고객 정보 조회")
            page -= 1
            info = custlist[page]
            key = list(info.keys())
            value = list(info.values())
            for i in range(len(info)) :
                print("%s : %s"%(key[i],value[i]))
            print('현재 페이지는 {}쪽 입니다'.format(page+1))
        else :
            print('페이지 이동이 불가합니다')
            print(page)        

    elif choice == 'N':
        if page < len(custlist)-1 :
            print("다음 고객 정보 조회")
            page += 1
            info = custlist[page]
            key = list(info.keys())
            value = list(info.values())
            for i in range(len(info)) :
                print("%s : %s"%(key[i],value[i]))
            print('현재 페이지는 {}쪽 입니다'.format(page+1))
        else :
            print('페이지 이동이 불가합니다')
            print(page)     
    elif choice=='D':
        print("고객 정보 삭제")
        ck = 0
        m = input("삭제할 고객의 이메일 : ")
        for i in range(0,len(custlist)) :
            if custlist[i]['email'] == m :
                del custlist[i]
                ck = 1
                print('삭제되었습니다')
                break 
        if ck == 1 :
            print('이메일이 존재하지 않습니다')            
     
        '''choice1 = input('삭제할 고객 이메일 :')
        delok = 0
        for i in range(0,len(custlist)) :
            if custlist[i]['email'] == choice1 :
                print('{}고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
                del custlist[i]
                print(custlist)
                delok = 1 #지우면 1로
                break

        if delok == 0:
            print('등록되지 않은 이메일 입니다.')
            print(custlist) <<쌤이한거'''        
    elif choice=="U": 
        print("고객 정보 수정")
        ck = 0
        sujung = input("수정할 고객의 이메일 : ")
        for i in range(0,len(custlist)) :
            if custlist[i]['email'] == sujung : 
                while True :
                    data =input('수정할 정보를 입력하세요 :')
                    if data in list(custlist[i].keys()) :
                        break
                data2 = input('수정할 내용을 입력 :')
                custlist[i][data] = data2
                ck =1
                break
        
        print(custlist)


        if ck == 1 :
            print('이메일이 존재하지 않습니다')        

        while False : #원래 True >> 쌤이한 거 코드 
            choice1 = input('수정할 고객 이메일 :')
            idx = -1
            for i in range(0,len(custlist)) :
                if custlist[i]['email'] == choice1 :
                    idx = i
                    break
            
            if idx == -1 :
                print('등록되지 않은 이메일')
                break

            choice2 = input('''
            다음중 수정하실 정보를 골라주세요
            name sex birthyear 
            수정할 정보가 없으면 'exit'입력''' )

            if choice2 in ('name','sex','birthyear'):
                custlist[idx][choice2] = input('수정할 {}를 입력하세요:'.format(choice2))
                break
            elif choice2 == 'exit' :
                break
            else :
                print('존재하지 않는 정보 ㅇㅇ')
                break        
    elif choice=="Q":
        print("프로그램 종료")
        break
    elif choice=="S":
        print("저장")
        f = open('info.txt','wb')
        pickle.dump(custlist,f)
        f.close()
    elif choice=="F" :
        print("불러오기")
        f = open('info.txt','rb')
        custlist = pickle.load(f)
        page = len(custlist)-1
        f.close()    
    else:
        print("잘못입력하셨습니다.")
