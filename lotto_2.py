import random
print("이번엔 될거야")
a = int(input())

for i in range(a):
    #lotto = random.sample(range(1,7),6)
    #print(lotto)
    lotto = random.sample(range(1,46),6)
    #print(lotto)
    for i in range(0,5):
        for j in range(i,6):
            if lotto[i] > lotto[j] :
                b = lotto[j]
                lotto[j] = lotto[i]
                lotto[i] = b             
            
    print(lotto)
    
