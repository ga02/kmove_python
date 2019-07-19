import pickle

data = {1:'python', 2:'you'}

f = open('test_p.txt','wb')

pickle.dump(data,f) #dumps는 파이썬 안에서 ㅑ
f.close()

f = open('test_p.txt','rb')
data1=pickle.load(f)
f.close()

print(data)
print(data1)
print(type)
