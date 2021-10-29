ant = []
for i in range(10):
    ant.append([])
    data = input().split(' ')
    for j in range(10):
        ant[i].append(int(data[j]))

x = 1
y = 1
while (True):
    ant[1][1]=9
    if ant[x][y+1]==0:
        ant[x][y+1]=9
        y+=1
    elif ant[x][y+1]!=0 and ant[x+1][y]==0:
        ant[x+1][y]=9
        x+=1
    elif ant[x+1][y]==2:
        ant[x+1][y]=9
        break
    elif ant[x][y+1]==2:
        ant[x][y+1]=9
        break
    elif ant[x][y+1]!=0 and ant[x+1][y]!=0:
        break
    elif x==9 and y==9:
        break

for i in range(10):
    for j in range(10):
        print(ant[i][j] ,end=' ')
    print()