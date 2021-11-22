n = int(input())
arr = []
for i in range(n):
    data = list(map(int, input().split(' ')))
    arr.append(data)

arr.sort(key=lambda x: (-x[0], -x[1], -x[2]))
# print(arr)

index = 0  
first = 1
second = 0
third = 0

for i in range(n-1):
    if sum(arr[i]) != sum(arr[i+1]):
        break    
    if sum(arr[i]) == sum(arr[i+1]):
        first += 1
        index += 1


# print(f'index = {index} first = {first} second = {second} third = {third}')
for i in range(index, n-1):
    if sum(arr[i]) == sum(arr[i+1]):
        index += 1
        second += 2
    if index > n-1:
        break
    else:
        index += 1
        second += 1
        break

# print(f'index = {index} first = {first} second = {second} third = {third}')
for i in range(index, n-1):
    if sum(arr[i]) == sum(arr[i+1]):
        index += 1
        third += 2
    if index > n-1:
        break
    else:
        index += 1
        third += 1
        break
# print(f'index = {index} first = {first} second = {second} third = {third}')

first *=100
second *=80
third *=50
print(first+second+third)
