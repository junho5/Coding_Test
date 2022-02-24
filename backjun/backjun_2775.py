time = int(input())
for _ in range(time):
    result = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    k = int(input())
    n = int(input())
    for i in range(k):
        for j in range(1,n):
            result[j] = result[j-1] + result[j]
    print(result[n-1])        