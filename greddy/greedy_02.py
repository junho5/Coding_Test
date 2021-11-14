# N은 배열의 크기 M은 숫자가 더해지는 횟수 K는 문제에 주어진 큰 수의 법칙 변수이다.
# 큰 수의 법칙 = 주어진 배열 숫자들중 M번 더하되 가장 큰수를 K번을 초과하게 더할수 없다.
N, M, K = map(int, input().split(' '))

data = list(map(int, input().split(' ')))

data.sort()

big = data[N-1]
pre_big = data[N-2]
score = 0
cnt = 1

while True:
    for i in range(K):
        if M == 0:
            break
        score += big
        M -= 1
    if M == 0:
        break
    score += pre_big
    M -= 1
print(score)
# 해당식은 K가 만약 1이였을 경우에 계속 나머지가 0이됨으로 문제가 있는 코드다.
# for i in range(M):
#     if cnt%K==0:
#         score += pre_big
#         cnt+=1
#     else:
#         score += big
#         cnt+=1
#     print(score)
# print(score)
