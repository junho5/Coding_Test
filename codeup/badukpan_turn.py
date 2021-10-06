answer = []
for i in range(19):
    answer.append([])
    for j in range(19):
        answer[i].append(0)

for i in range(19):
    a=input().split(' ')
    for j in range(19):
        a[j]=int(a[j])
        answer[i][j]=a[j]

n=int(input())
for i in range(n):
    a,b=input().split(' ')
    x=int(a)
    y=int(b)
    for j in range(19):
        if answer[x-1][j]==0:
            answer[x-1][j]=1
        else:
            answer[x-1][j]=0
        if answer[j][y-1]==0:
            answer[j][y-1]=1
        else:
            answer[j][y-1]=0

for i in range(19):
    for j in range(19):
        print(answer[i][j], end=' ')    
    print() 