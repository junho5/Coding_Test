while(True):
    answer = list(map(int,input().split()))
    answer.sort()
    if answer[0] ==0 and answer[1] ==0 and answer[2] ==0:
        break
    elif answer[2]**2 == answer[0]**2 + answer[1]**2:
        print('right')
    else:
        print('wrong')


