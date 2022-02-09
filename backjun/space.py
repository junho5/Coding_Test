alpha = [-1]*26
n =input()
my_list=[]
for i in range(len(n)):
    space = ord(n[i])-ord('a')
    alpha[space] = space
    my_list.append(space)

for i in range(5):
    print(my_list[i])
    print(my_list.index(my_list[i]))

        
        
    
    
print(alpha)       
print(my_list)
# for i in alpha:
#     print(i,end=' ')