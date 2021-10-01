a= int(input())
b= input().split()
c=[]
for i in range(a):
    c.append(int(b[i]))
c.reverse()
for i in range(a):
    print(c[i],end=' ')
