T = int(input())
for i in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    arr_90 = [[0] * n for _ in range(n)]
    arr_180 = [[0] * n for _ in range(n)]
    arr_270 = [[0] * n for _ in range(n)]
    for col in range(n):
        for row in range(n):
            arr_90[row][n-col-1] = matrix[col][row]
            arr_180[n-col-1][n-row-1] = matrix[col][row]
            arr_270[n-row-1][col] = matrix[col][row]

    print('#{}'.format(i))
    for col in range(n):
        print(''.join(list(map(str, arr_90[col]))), end=' ')
        print(''.join(list(map(str, arr_180[col]))), end=' ')
        print(''.join(list(map(str, arr_270[col]))))