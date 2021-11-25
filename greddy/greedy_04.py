# 최대한 많이 나누기 N 값에 대해서 K로 나눈다 이때 나눠질경우는 나누고 나누어지지 않을 경우는 1을 뺸다 1이되는 최소횟수를 출력하라
N, K = map(int,input().split(' '))

cnt = 0
while True:
    if N==1:
        break
    if N%K==0:
        N/=K
        cnt+=1
    else:
        N-=1
        cnt+=1
print(cnt)


