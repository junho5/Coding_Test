sugar = int(input())
three = sugar // 3
result = []
result2 = []
for i in range(three+1):
    num = sugar
    num -= i * 3
    if num % 5 == 0:
        result.append(i+(num//5))
        result2.append('o')
    else:
        result2.append('x')
if 'o' in result2:                    
    print(min(result))
else:
    print(-1)    
    
# sugar = int(input())

# bag = 0
# while sugar >= 0 :
#     if sugar % 5 == 0 :  # 5의 배수이면
#         bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bag)
#         break
#     sugar -= 3  
#     bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
#     print(sugar)
# else :
#     print(-1)    
    