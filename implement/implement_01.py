n = int(input())

x,y = 1,1

move_type=['L','R','U','D']
move_x = [-1,1,0,0]
move_y = [0,0,-1,1]

type = input().split(' ')

for type in type:
    for i in range(len(move_type)):
        if type==move_type[i]:
            dx = x + move_x[i]
            dy = y + move_y[i]
    if dx<1 or dy<1 or dx>n or dy>n:
        continue
    x,y = dx, dy

print(x,y)
            
