import math

n = int(input())
answer = []
store = 100
for i in range(n):
    num = int(input())
    result = [True] * (num + 1)
    
    for j in range(2,int(math.sqrt(num)+1)):
        if result[j] == True:
            for k in range(j+j,num+1,j):
                result[k] = False
                
    prime = [i for i in range(2,num+1) if result[i]==True]
    
    # print(prime)
    
    for i in range(len(prime)):
        for j in range(len(prime)):
            temp = prime[i] + prime[j]
            if temp == num:
                minus = abs(prime[i]-prime[j])
                if store > minus:
                    store = minus
                    answer = []
                    answer.append(prime[i])
                    answer.append(prime[j])             
    for i in answer:
        print(i, end=' ')
    print('')
    answer = []
    store = 100
    