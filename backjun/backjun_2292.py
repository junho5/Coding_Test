n = int(input())
bee = 1
cnt = 0
while(True):
    if n == 1:
        cnt += 1
        break
    elif bee == n:
        cnt += 1
        break
    elif n >= bee:
        cnt += 1
        bee += 6*cnt
    elif n < bee:
        cnt += 1
        break
print(cnt)

# n = int(input())

# nums_pileup = 1  # 벌집의 개수, 1개부터 시작
# cnt = 1
# while n > nums_pileup :
#     nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
#     cnt += 1  # 반복문을 반복하는 횟수
# print(cnt)
