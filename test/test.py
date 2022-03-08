import math
import sys

result = [True] * 10001
for i in range(2,int(math.sqrt(10001))):
    if result[i] == True:
        for j in range(i+i,10001,i):
            result[j] = False
            
n = a = int(sys.stdin.readline())

for i in range(n):
    answer = []
    minus = []
    num = int(sys.stdin.readline())

    prime = [i for i in range(2,num+1) if result[i]==True]
    # print(prime)
    index = len(prime) // 2
    for j in range(index,len(prime)):
        if num - prime[j] in prime:
            answer.append([prime[j],num-prime[j]])
            minus.append(prime[j]-(num-prime[j]))
    min_index = minus.index(min(minus))
    answer[min_index].sort()
    for i in answer[min_index]:
        print(i, end = ' ')
    print('')
        