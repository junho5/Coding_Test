time = int(input())
for time in range(time):
    pan = []
    temp = 0
    result = 0
    n,m = map(int,input().split())
    cnt = abs(n-m)+1
    for j in range(n):
        row = list(map(int,input().split()))
        pan.append(row)
    for i in range(n):
        for j in range(n):
            temp = 0
            for a in range(m):
                for b in range(m):
                    if a+i > n-1 or b+j > n-1: # 수정부분
                        break
                    else:
                        temp += pan[a+i][b+j]
                        if temp > result:
                            result = temp
    print(f"#{time+1} {result}")