#числовая угадайка
import random

def is_valid(value):
    return value.isdigit() and int(value)>0

def guess_numbers():
    while True:
        value = input('Введите число: ')
        if is_valid(value):
            return value
        else:
            print('Ошибка, введено неккоректное число')

            

def game():
    print('Правая граница')
    right_border = guess_numbers()
    right_number = random.randint(1, int(right_border))
    cnt_tries = 0
    while True:
        user_number = input('введите ваше число или exit, если хотите выйти:  ')
        if is_valid(user_number) and int(user_number)<=int(right_border):
            user_number = int(user_number)
            cnt_tries+=1
            if right_number == user_number:
                return 'Победа', cnt_tries
            elif right_number > user_number:
                print('Загаданное число больше')
            elif right_number < user_number:
                print('Загаданное число меньше')
        elif user_number.lower()=='exit':
            return 'Поражение', cnt_tries
        else:
            print('Ошибка, введено неккоректное число')
            
while True:
    turniers = game()
    if turniers[0] == 'Победа':
        print('Вы победили за ', turniers[1], 'ходов')
    else:
        print('игра прервана. Кол-во ходов: ', turniers[1])
    user_wish = input('желаете сыграть еще раз? (Да/Нет): ')
    if user_wish.lower() == 'да':
        continue
    else: break

print('Спасибо за игру')

