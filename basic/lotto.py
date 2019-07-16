import random
list = []
for i in range(1,6) :
    for j in range(1,7) :
        n = random.randint(1,45)
        while list.count(n) > 0 :
            n = random.randint(1,45)
        list.append(n)
    list.sort()
    print('로또 :',list)   
    list.clear() 

