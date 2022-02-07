num_list = []
result = []
for i in range(1,101):
    num_list.append(i)

for i in num_list:
    first = i//10
    second = i%10
    new_num = i+first+second
    result.append(new_num)
    
print(sorted(result))
    