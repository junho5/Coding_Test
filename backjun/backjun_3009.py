result1 = []
result2 = []
result3 = []
for i in range(3):
    x,y =map(int,input().split())
    result1.append(x)
    result2.append(y)

set_x =set(result1)
set_y =set(result2)

for i in result1:
    if result1.count(i) == 1:
        result3.append(i)
        
for i in result2:
    if result2.count(i) == 1:
        result3.append(i)

for i in result3:
    print(i,end=' ')   