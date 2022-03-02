import sys
m,n = map(int,sys.stdin.readline().split(' '))

result = []

for i in range(m,n+1):
    check = 0
    for j in range(1,i+1):
        if i % j ==0:
            check +=1
    if check == 2:
        print(i)
        # result.append(i)
        continue
        
# for i in result:
#     print(i)