# rstrip는 readline이 개행문자 /n도 저장하기 때문에 공백삭제라고 생각하면됨
# int형으로 형변환하면 어쩌피 없어지니깐 상관 x

import sys

data = sys.stdin.readline().rstrip()

print(data)

# input같은 경우 시간을 많이 잡아먹기 때문에 sys를통해 시간을 절약한다.

print(f"{data}")


# import sys

# x= int(input())
# for i in range(x):
#     a,b = map(int,sys.stdin.readline().split(' '))
#     print(a+b)
