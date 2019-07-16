listdata = []

while True :    
    print('''
    ================리스트 데이터 관리=================
    1. 데이터 추가 2. 데이터 수정 3. 리스트 삭제 4.종료
    ''')

    menu = int(input("메뉴를 선택하세요\n"))
    
    if menu == 4 :
        break
    elif menu == 1 :
        data = input("추가할 데이터를 입력하세요^*^\n")
        listdata.append(data)
        print(listdata)
    elif menu == 2 :
        print(listdata)
        n = int(input("몇 번째 데이터를 수정하시겠습니까?!?\n"))
        while n > len(listdata) :
            n = int(input("다시 입력해주세요^^"))

        v = input("수정할 데이터를 입력해주세요^^\n")
        
        listdata[n-1] = v
        print(listdata)
        print('수정되었습니다^^')
    elif menu == 3 :
        print(listdata)
        n = int(input('몇 번째 데이터를 삭제하시겠습니까?!?'))
        while n > len(listdata) :
            n = int(input("다시 입력해주세요^^"))
        del listdata[n-1]
        print(listdata)
        print('삭제되었습니다^^')
    else :
        print("메뉴를 다시 입력해주세요^^")

    # range(1,11) 인덱스 1부터 10까지
