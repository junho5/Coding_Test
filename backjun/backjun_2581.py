m = int(input())
n = int(input())

result = []
for i in range(m,n+1):
    check = 0
    for j in range(1,i+1):
        if i % j == 0:
            check += 1
    if check == 2:
        result.append(i)
if len(result)<1:
    print(-1)
else:
    print(sum(result))
    print(min(result))