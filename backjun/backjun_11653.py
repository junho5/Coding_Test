n = int(input())

result = []
for i in range(n+1):
    check = 0
    for j in range(1,i+1):
        if i % j ==0:
            check +=1
    if check ==2 and n%i==0:
        result.append(i)

result2 = []
for i in result:
    while(n%i==0):
        if n % i == 0:
            n //= i
            result2.append(i)
        else:
            continue

for i in result2:
    print(i)    