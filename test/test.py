input_num = input()
store = input_num
cnt = 0

while(True):
    if int(input_num)<10:
        input_num = int(input_num)*10
        cnt +=1
    else:
        second = (int(input_num[0])+int(input_num[1]))%10
        first = input_num[1]
        input_num = first + str(second)
        cnt+=1
        print(input_num)
    if store == input_num:
        break
print(cnt)