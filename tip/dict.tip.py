a={'사과': 'apple'} # 이 방법은 처음에 나중에 하면 초기화 되버림 
a['바나나']='banana'
a[2]='two'

b=dict()
b={'오렌지':'orange'} # 이 방법은 처음에 나중에 하면 초기화 되버림
b[1]='one'
b['melon']='멜론'

print(a['사과'])
print(a[2])
print('----------------------')
print(b['오렌지'])
print(b.keys())
print('----------------------')
for i in a.keys():
    print(i)
print('----------------------')
for i in a.values():
    print(i)
print('----------------------')
print(a.values())
print(a.keys())
print(a.items())
print('----------------------')

a.clear() # 다 지우기
print(b['melon'])
print(b.get('melon'))
print('----------------------')
print('melon' in b)
print('----------------------')


