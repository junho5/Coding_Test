n, m = map(int,input().split())

num = list(map(int,input().split()))
num.sort()

max_num = -1
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n): 
            temp = 0
            temp += num[i]
            temp += num[j]
            temp += num[k]
            if temp > max_num and temp <= m:
                max_num = temp
print(max_num)
        