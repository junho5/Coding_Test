# 필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
# 단, 소수점 셋째 자리에서 반올림하여 둘째 자리까지 출력한다. 
a,b,c=input().split(' ')
a=int(a)
b=int(b)
c=int(c)
total = (((a*b*c)/8)/1024)/1024
total = round(total,2)
print('{:.2f} MB'.format(total))

