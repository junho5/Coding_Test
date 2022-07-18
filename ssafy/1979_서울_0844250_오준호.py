T = int(input())
for time in range(T) :
    pan = []
    total = 0
    n, m = map(int, input().split())
    for j in range(n):
        row = list(map(int,input().split()))
        pan.append(row)
    for i in range(n) :
        cnt = 0
        for j in range(n) :
            if pan[i][j] == 1 :
                cnt += 1
            if pan[i][j] == 0 or j == n -1 :
                if cnt == m :
                    total += 1
                if pan[i][j] == 0 :
                    cnt = 0
    for i in range(n) :
        cnt = 0
        for j in range(n) :
            if pan[j][i] == 1 :
                cnt += 1
            if pan[j][i] == 0 or j == n - 1 :
                if cnt == m :
                    total += 1
                if pan[j][i] == 0 :
                    cnt = 0
 
    print(f"#{time+1} {total}")
