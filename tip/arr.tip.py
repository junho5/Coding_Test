# set은 중복 제거
my_list = []
for i in range(10):
    num = int(input())
    my_list.append(num%42)
my_set = set(my_list)

print(len(my_set))  

# count는 갯수 확인 가능
a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))
    
# index는 index확인 가능
list = []
cnt = 0
for i in range(9):
    num = int(input())
    list.append(num)
for i in range(9):
    if list[i] != max(list):
        cnt +=1
print(max(list))
print(list.index(max(list))+1)


