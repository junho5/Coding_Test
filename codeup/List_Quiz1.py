answer = []
for i in range(5):
    answer.append([])

for i in range(5):
    a=input().split(' ')
    for j in range(5):
        a[j]=int(a[j])
        answer[i].append(a[j])
# for i in range(5):
#     for j in range(5):
#         print(answer[i][j], end=' ')    
#     print() 

n=int(input())
for i in range(n):
    a,b=input().split(' ')
    a=int(a)
    b=int(b)
    for j in range(n):
        if a==answe