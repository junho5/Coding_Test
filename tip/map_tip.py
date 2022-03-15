n = int(input())  

for i in range(1, n+1):   
    num = list(map(int, str(i))) # 숫자 각각 나누어서 리스트 저장 ex) 101 = [1][0][1]
    print(num)
    
n = int(input())  

for i in range(1, n+1):   
    num = sum(map(int, str(i))) # 숫자 각각 나누어서 더한 값 ex) 101 => 1 + 0 + 1 = 2 , 23 => 2 + 3 = 5
    num_plus = i + num
    print(num)