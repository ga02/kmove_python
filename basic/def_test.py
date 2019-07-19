'''def add(a,b) : #매개변수 ab
    return a + b #무조건 0개또는 1개

print(add(5,4)) #5,4 = 인수 ! 
c = add(1234,523)   
print(c)'''



'''def add(choice,*a) :
    print(type(a))
    print(a)
    result = 0
    for i in a :
        result = result + i
    return result

print(add(1,3,5,7,9))

def onestar(*x) :
    print(type(x))
    for i in x :
        print(i,end='')


def twostar(**x) :
    print(x)

onestar('남','가','영','짱')
twostar()  ''' # 안됌

'''def add_and_mul(a,b) : ###!!!!! 알아서 나눠줌 !!!!! 리턴값 두개 변수값 두개에넣으면
    return a+b,a*b

add,mul = add_and_mul(3,6)
total = add_and_mul(2,5)
print(type(add))
print(type(mul))
print(total)
print(add)
print(mul)    

def say_myself(name,old,man=False) : 
    print('나의 이름은 %s 입니다'%name)
    print('나이는 %d살입니다'%old)
    if man :
        print('남자')
    else :
        print('여자입니다') 

say_myself('',0)
say_myself('남가영',25)
say_myself('허영욱',25,True)'''

a=1
alist=[1,2,3]

def add_data(a):
    a=2
    alist.append(4)
    print(a)

add_data(a)
print("바깥쪽 %d"%a)