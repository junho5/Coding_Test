answer = [-1]*26
n =input()
word=[]
for i in range(len(n)):
    space = ord(n[i])-ord('a')
    word.append(space)

for i in range(len(n)):
    index = word[i]
    if answer[index] == -1:
        answer[index] = word.index(word[i])

for i in answer:
    print(i,end=' ')


# find 함수는 찾는 숫자가 존재하지 않는 경우에는 -1을 반환한다.
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x)),end=' ') 