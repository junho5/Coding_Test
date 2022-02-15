word = input()
cnt = 0
for i in range(len(word)):
    if word[i] == 'd' and i+1 <len(word) and word[i+1] == 'z':
        cnt += 1
    elif word[i] == 'l' and i+1 <len(word) and word[i+1] == 'j':
        cnt += 1
    elif word[i] == 'n' and i+1 <len(word) and word[i+1] == 'j':
        cnt += 1    
    else:
        cnt += 1
print(cnt)