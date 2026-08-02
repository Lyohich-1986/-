from random import randrange, seed
a = []
seed(1)
for i in range(100):
    a.append(randrange(0, 101))
#пузырек
for i in range(len(a)-1): 
    cnt = 0
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            cnt=1
    if cnt==0:
        break
print(a)    
#выбором

for i in range(len(a)-1):
    best = i
    for j in range(i+1, len(a)):
        if a[j]<a[best]:
            best = j
    a[i], a[best] = a[best], a[i]
    
print(a)



for i in range(1, len(a)):
    j = i
    elem = a[j]
    while j>0 and a[j-1]> elem:
        a[j] = a[j-1]
        j-=1
    a[j] = elem 


print(a)
