# n을 입력하였을때 0시 0분 0초부터 n시 59분 59초 까지의 n이 들어간 횟수를 출력하시오

N = int(input())
cnt = 0

for i in range(0, N+1):
    for j in range(10):
        for k in range(10):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)
