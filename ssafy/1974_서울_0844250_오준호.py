T = int(input())
for time in range(T):
    answer = 1
    plus = 0
    arr = []
    check = [[]*9 for _ in range(9)]
    check2 = [[]*9 for _ in range(9)]
    for i in range(9):
        row = list(map(int,(input().split())))
        arr.append(row)
    list_num = 0
    for i in range(9):
        if i == 3:
            plus = 3
        elif i == 6:
            plus = 6
        for j in range(9):
            list_num = j // 3
            check[list_num+plus].append(arr[i][j])
    for i in range(9):
        for j in range(9):
            check2[j].append(arr[i][j])
    for i in range(len(arr)):
        arr[i] = set(arr[i])
        if len(arr[i]) < 9:
            answer = 0
    for i in range(len(check)):
        check[i] = set(check[i])
        if len(check[i]) < 9:
            answer = 0
    for i in range(len(check2)):
        check2[i] = set(check2[i])
        if len(check2[i]) < 9:
            answer = 0
    print(f"#{time+1} {answer}")

