input_num = input()
store = int(input_num)
cnt = 0

while(True):
    if int(input_num)<10:
        input_num = int(input_num)*11
        cnt +=1
        input_num = str(input_num)
    else:
        second = (int(input_num[0])+int(input_num[1]))%10
        first = int(input_num[1])
        input_num = str(first) + str(second)
        cnt+=1
    if store == int(input_num):
        break
print(cnt)