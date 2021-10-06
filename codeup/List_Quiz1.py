answer = []
for i in range(20):
    answer.append([])
    for j in range(20):
        answer[i].append(0)

for i in range(19):
    a=input().split(' ')
    for j in range(19):
        a[j]=int(a[j])
        answer[i+1][j+1]=a[j]

n=int(input())
for i in range(n):
    a,b=input().split(' ')
    a=int(a)
    b=int(b)
    for j in range(1,20):
        if answer[a][j]==0:
            answer[a][j]=1
        else:
            answer[a][j]=0
        if answer[j][b]==0:
            answer[j][b]=1
        else:
            answer[j][b]=0

for i in range(1,20):
    for j in range(1,20):
        print(answer[i][j], end=' ')    
    print() 