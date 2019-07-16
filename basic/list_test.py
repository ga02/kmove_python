a=[]
b=[1,2,3]
c=['life','is']
d=[1,2,'life',3,4,5]
e=[1,2,[1,2,3]]

print(a)
print(b)
print(c)
print(d)
print(e)
#주석주석 샵은 주 석 

print(d[-4])
#print(d[1]+d[2]) 다른데이터형끼리 계산 안됌

a=[1,2,3,4]

a[3] = 6

print(a)
del a[0]
print(a)

a.append(7) # .찍어서 접근하는 함수는 클래스의 하위요소? 함수(리스트의 하위요소) / insert는 위치정해서 삽입

print(a)#이런건 걍 내장된함수

a=[2,5,3,7,13,9]
print(a)
a.sort()
print(a)
a.sort(reverse=True) #revers는 내림차순
print(a)
n= a.index(5)
print(n)

#튜플은 한개의 값만 적을때 , 필수/ 괄호를 안해도됌 

#딕셔너리는 인덱스x(순서가 없음) / 키값을 접근 키는 중복x 

dic = {1:10, 2:{40}} #{}값만 들어간거 셋 ?
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get(1))

print(1 in dic)

food = ['화반','오이시카타','토도','이삭','황금룡','맥날']

input("시작하려면 0을 입력하세요! ")

    





