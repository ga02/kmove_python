money = True

if money :
    print("택시")
else :
    #pass 안에 내용을 비워 놓을 때
    print("걸어감")

#else if 여기서는 elif

jumsu = input("성적 :\n") #여기서 바로 int()해서 인트형으로 저장하면 더 간편
print(jumsu) #받는 값은 기본적으로 스트링

print('성적은 ',end='')
if v > 80 :
     print('A')
elif v > 60 or v < 80 :
    print('B')
elif v > 40 or v < 60 :
    print('C')
elif v > 20 or v < 40 :
    print('D')
else:
    print('F')

#print ('성적은 %s 입니다 ~~'%)
#print('입력한 성적은',jumsu) 이거는 인트로 바꿔서 데이터형 같아져서 가능 
    
