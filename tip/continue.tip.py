for i in range(2,10):
    for j in range(1,10):
        if i%2 ==0:
            continue
        print('{} * {} = {}'.format(i,j,i*j))
    print(' ')