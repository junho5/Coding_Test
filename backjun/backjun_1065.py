n = int(input())

cnt = 0

for i in range(1,n+1):
    if i<100:
        cnt +=1
    else:
        num = str(i)
        empty = []
        for j in range(len(num)):
            empty.append(num[j])
        empty_int = list(map(int,empty))
        for k in range(1):
            if empty_int[k]-empty_int[k+1] == empty_int[k+1]-empty_int[k+2]:
                cnt+=1
print(cnt)