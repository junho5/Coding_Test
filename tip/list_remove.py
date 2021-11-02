result=[1,2,3,4,5,5,5]
remove_number=[3,5]


result= [i for i in result if i not in remove_number ]

print(result)