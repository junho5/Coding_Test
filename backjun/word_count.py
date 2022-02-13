n = input().split()

for i in n:
    if i== '' or i==' ':
        n.remove(i)
print(len(n))