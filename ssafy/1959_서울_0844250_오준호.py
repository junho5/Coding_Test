time = int(input())
result = 0

for i in range(time):
    n,m = map(int,input().split())
    result = 0
    first = list(map(int,input().split()))
    second = list(map(int,input().split()))
    if len(first)>len(second):
        big = first
        small = second
    else:
        big = second
        small = first
    for j in range(abs(n-m)+1): 
        temp = 0
        for k in range(len(small)): 
            temp += big[k+j] * small[k]
        if temp > result:
            result = temp
    print(f"#{i+1} {result}")