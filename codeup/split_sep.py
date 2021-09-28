# 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
a, b = input().split(':')
print(a, b, sep=':')


# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
y, m, d = input().split('.')
print(d, m, y, sep='-')
