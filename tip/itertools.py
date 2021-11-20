# 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리

from itertools import permutations
# 만들수 있는 모든 순열 출력 (숫자로 개수 지정가능)
data = ['A', 'B', 'C']
data = list(permutations(data, 2))
print(data)

from itertools import product
# 만들수있는 모든 순열 출력 (숫자로 개수 지정가능, 중복 허용)
data = ['A', 'B', 'C']
data = list(product(data, repeat=2))
print(data)

print('-----------------------------------------------------------------------------------------------------------------------------')

from itertools import combinations
# 만들수있는 조합 출력 (숫자로 개수 지정가능)
data = ['A', 'B', 'C']
data = list(combinations(data, 2))
print(data)

from itertools import combinations_with_replacement
# 만들수있는 조합 출력 (숫자로 개수 지정가능, 중복 허용)
data = ['A', 'B', 'C']
data = list(combinations_with_replacement(data, 2))
print(data)