from random import randint


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers
print(generate_numbers())

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    while len(new_guess)<3:
        num = int(input(f'{len(new_guess)+1}번째 숫자를 입력하세요'))
        if num<0 or num>9:
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
        elif num in new_guess:
            print('중복되는 숫자입니다. 다시 입력하세요.')
        else:
            new_guess.append(num)
            
            
        
    return new_guess

print(take_guess())