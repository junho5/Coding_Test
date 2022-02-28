n = int(input())

num = map(int,input().split())

answer = 0
for i in num:
    check = 0
    for j in range(1,i+1):
        if i == 1:
            pass
        if i % j == 0:
            check += 1
    if check == 2:
        answer += 1

print(answer)