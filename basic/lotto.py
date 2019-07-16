import random
list = []
for i in range(1,6) :
    for j in range(1,7) :
        n=0
        while list.count(n) > 1 :
            n = random.randint(1,45)
