result = set([1, 1, 2, 3, 4, 5])  # 중복허용하지않음 , 순서없음
result2 = {1, 1, 3, 5, 6, 7, 8}  # 동일한 초기화 방법

print(result)
print('----------------------')
print(result | result2)  # 합집합
print(result & result2)  # 교집합
print(result - result2)  # 차집합
print('----------------------')

result3 = {0, 1}
result3.add(2)  # 추가
result3.update([3, 4, 5])  # 여러 값 추가
result3.remove(0)  # 특정값 삭제
print(result3)
