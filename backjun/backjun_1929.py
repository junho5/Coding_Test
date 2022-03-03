import math

# n, m = map(int, input().split())
# sqrt_m = int(math.sqrt(m))
# result = [True] * (m+1)
# for i in range(2,sqrt_m+1):
#     if result[i] == True:
#         for j in range(i+i,m+1,i):
#             result[j] = False
            
# # print([i for i in range(2,m+1) if result[i]==True and n<=i])

# for i in range(n,m+1):
#     if result[i] == True and i>1:
#         print(i)
        
        
# ===========================================================================================
n, m = map(int, input().split())

def isprime(n, m):
  prime = [True] * (m+1)                # n개의 [True]가 있는 리스트 생성
  for i in range(2, int(math.sqrt(m))+1): # n의 제곱근까지만 검사
    if prime[i]:                    # prime[i]가 True일때
      for j in range(i+i, m+1, i):    # prime 내 i의 배수들을 False로 변환
        prime[j] = False

  for i in range(n, m+1):
    if i > 1 and prime[i] == True:  # 1 이상이면서 남은 소수들을 출력
      print(i)

isprime(n, m)