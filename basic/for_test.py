for i in range(2,10) :
    for j in range(1,10):
        print("%d * %d = %d" %(i,j,i*j))
    print()

for i in range(1,10) :
    for j in range(2,10) :
        print("%d * %d = %-2d     "%(j,1,i*j),end='')
    print()