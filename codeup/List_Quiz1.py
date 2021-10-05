answer = []
for i in range(5):
    answer.append([])

for i in range(5):
    a=input().split(' ')
    for j in range(5):
        a[j]=int(a[j])
        answer[i].append(a[j])