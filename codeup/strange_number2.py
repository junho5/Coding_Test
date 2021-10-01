a= int(input())
b= input().split()
c=[]
for i in range(a):
    b.append(int(b[i]))

b.reverse()
for i in range(a):
    print(b[i],end=' ')
