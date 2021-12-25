def factorial_iteration(i):
    result = 1 
    for i in range(1,i+1):
        result *= i
        # print(f"{i}번쨰 값은 {result} 입니다.")
    return result
    
print(factorial_iteration(5))

def factorial_recursive(i):
    if i<=1:
        return 1
    return i * factorial_recursive(i-1)
    
print(factorial_recursive(5))

def fivonachi(i):
    if i == 0 :
        return 0
    if i ==1 or i==2:
        return 1
    return fivonachi(i-1) + fivonachi(i-2)

print(fivonachi(7))