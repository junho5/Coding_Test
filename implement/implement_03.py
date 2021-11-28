map = input()

row = int(map[1])
column = int(ord(map[0])) - int(ord('a'))+1
check = 0
move_type = [(-2, 1), (-2, -1), (1, -2), (-1, -2),
             (2, -1), (2, 1), (1, 2), (-1, 2)]

for move in move_type:
    plus_row = row + move[0]
    plus_column = column + move[1]
    # 이렇게도 가능한데 밑에 있는게 더 깔끔
    # check +=1
    # if plus_row>8 or plus_row<1:
    #     plus_row = plus_row - move[0]
    #     check -= 1
    #     continue
    # if plus_column>8 or plus_column<1:
    #     plus_column = plus_column - move[1]
    #     check -= 1
    #     continue
    if plus_row >= 1 and plus_row <= 8 and plus_column >= 1 and plus_column <= 8:
        check += 1

print(check)
