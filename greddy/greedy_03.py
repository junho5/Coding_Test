# 행에서 가장 작은 숫자를 뽑을때 가장 큰 값을 가지고 있는 행의 작은값 가져온다
N, M = map(int,input().split(' '))

result = 0

for i in range(N):
    data = list(map(int,input().split(' ')))
    min_value = min(data)
    result = max(result,min_value)

print(result)    
