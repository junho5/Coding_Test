import math

result = [True] * 10001
for i in range(2,int(math.sqrt(10001))):
    if result[i] == True:
        for j in range(i+i,10001,i):
            result[j] = False

prime = [i for i in range(2,10001) if result[i]==True]
            
n = int(input())

for i in range(n):
    num = int(input())
    for j in range(num//2,num+1):
        if num-j in prime and j in prime:
            print(num-j,j)
            break 
    