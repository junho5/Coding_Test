import math

time = int(input())
for i in range(time):
    h,w,n = map(int,input().split())
    x=0
    y=0
    for j in range(n):
        if y == h:
            y = 0
        y += 1
    x = math.ceil(n/h)
    if x<10:
        x='0'+str(x)
    print(f'{y}{x}')