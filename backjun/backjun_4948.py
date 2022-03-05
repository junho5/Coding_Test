import math

while(True):
    n = int(input())
    double_n = 2*n
    prime = [True] * (double_n+1)
    result = []
    if n == 0:
        break
    else:
        for i in range(2,int(math.sqrt(double_n))+1):
            if prime[i] == True:
                for j in range(i+i,double_n+1,i):
                    prime[j] = False
    length = [i for i in range(n+1,double_n+1) if prime[i] ==True]
    print(len(length))