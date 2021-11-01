# 조건문을 넣어서 리스트 초기화 하는 방법
array = [i for i in range(20) if i % 2 == 0]
print(array)

# 2차원 리스트 0으로 초기화 하는방법
# 여기서 언더바는 숫자 안쓸때 사용
n = 3
m = 4
array2 = [[0]*n for _ in range(m)]
print(array2)
