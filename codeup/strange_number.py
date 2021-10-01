cnt = int(input())
teacher_speak = input().split(' ')
empty = []
for i in range(cnt):
    teacher_speak[i] = int(teacher_speak[i])

for i in range(24):
    empty.append(0)

for i in range(cnt):
    empty[teacher_speak[i]] += 1

for i in range(1, 24):
    print(empty[i], end=' ')
