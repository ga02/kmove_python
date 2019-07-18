import random
import time

word = [ 'family','돈까스','경찰청창살','아메리카노','apology']


input("시작하시려면 엔터를 눌러주세요~!")
t1 = time.time()
count = ['0','0','0','0','0']

for i in word :
    q='0'
    while count[word.index(q)]!=0 :
        q = random.choice(word)
    
    for j in range(len(word)) :
        if word[j] == q :
            count[j] = count[j]+1
    
    print(q)
    inp = input('입력 :')

    while q != inp :
        print('틀렸습니다!')
        print(q)
        inp = input('입력 :')

    
t2 = time.time()
t = t2 - t1

print('총 %.0f초 걸렸습니다'%t)

#썜 와일조건에 맞춰야할개수보다 작을때 들어가게 그리고 문제내고 입력받고 if 같으면 n+1, 통과 


    



