time = int(input())

for _ in range(time):
    n,word = input().split(' ')
    n = int(n)
    for i in word:
        for j in range(n):  
            print(i,end='')
    print('')