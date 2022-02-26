num_list = []
spare = []
for i in range(1, 10001):
    num_list.append(i)

num_list = list(map(str, num_list))
for i in num_list:
    new_num = int(i)
    for j in range(len(i)):
        new_num += int(i[j])
    spare.append(new_num)

spare = sorted(set(spare))

answer = []
for i in range(1, 10001):
    answer.append(i)

for i in spare:
    if i in answer:
        answer.remove(i)

for i in answer:
    print(i)
