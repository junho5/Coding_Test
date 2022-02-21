time = int(input())
error = 0
answer = []
score = 0

for i in range(time):
    word = list(input())
    for j in set(word):
        for k in range(len(word)):
            if j == word[k] and j not in answer:
                answer.append(k)
        for l in range(len(answer)-1):
            if abs(answer[l] - answer[l+1]) > 1:
                error += 1
        answer = []
    if error == 0 :
        score += 1
    else:
        error = 0

print(score)
            