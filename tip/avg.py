n = int(input())
answer_list = []
for i in range(n):
    my_list = list(map(int,input().split(' ')))
    people = my_list[0]
    sum = 0
    for j in range(1,len(my_list)):
        sum += my_list[j]
    avg = sum/(len(my_list)-1)
    cnt = 0
    for k in range(1,len(my_list)):
        if avg<my_list[k]:
            cnt +=1
    answer = (cnt/(len(my_list)-1))*100
    answer_list.append(answer)
    
for i in range(len(answer_list)):
    print('{:.3f}%'.format(round(answer_list[i],3)))