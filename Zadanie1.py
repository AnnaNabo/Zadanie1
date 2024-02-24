import random
#перенос минимального максимального значения немного сокращает количество итеарций в циклах
n =500 

A = list()

for i in range(n):
    ch = random.randint(1, 100)
    A.append(ch)

Acopy = A.copy()
#без переноса минмакс 
swap = True

k = 0

while swap == True:
    
    swap = False
    
    for j in range(len(Acopy) - 1):

        for i in range(len(Acopy) - 1):
            if Acopy[i] > Acopy[i + 1]:
               k +=1
               Acopy[i], Acopy[i + 1] = Acopy[i + 1], Acopy[i] 

print(Acopy)
print(k)    


minCh = A[0] 
maxCh = A[len(A) - 1]
min_index = 0
max_index = len(A) - 1

for j in range(len(A) - 1):
    if minCh > A[j]:
        minCh = A[j]
        min_index = j
    if maxCh < A[j]:
        maxCh = A[j]
        max_index = j

print(A)

if min_index < max_index:        
    A.pop(min_index)
    A.pop(max_index)
else:
    A.pop(max_index) 
    A.pop(min_index)

A.append(maxCh)
A.insert(0, minCh)

print(A)

#с переносом минмакс 
swap = True

k = 0

while swap == True:
    
    swap = False
    
    for j in range(len(A) - 1):

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
               k +=1
               A[i], A[i + 1] = A[i + 1], A[i] 

print(A)
print(k)