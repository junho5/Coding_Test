n = int(input())
arr = []
for i in range(n):
    data = list(map(int, input().split(' ')))
    arr.append(data)

arr.sort(key=lambda x: (-x[0], -x[1]))
print(arr)

index = 0
first = 1
second = 0
third = 0

for i in range(n-1):
    if sum(arr[i]) == sum(arr[i+1]):
       index += 1
       first += 1

print(index, first, second, third)
for i in range(index, n-1):
    if index >= n-1:
        break
    else:
        index += 1
        second += 1
    if sum(arr[i]) == sum(arr[i+1]):
       index += 1
       second += 1
print(index, first, second, third)

for i in range(second, n-1):
    if index >= n-1:
        break
    else:
        index += 1
        third += 1
    if sum(arr[i]) == sum(arr[i+1]):
       index += 1
       third += 1
print(index, first, second, third)

print(first*1000000)
print(second*500000)
print(third*100000)
