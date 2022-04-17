import random

num = random.randint(1, 100)

print('Добро пожаловать в числовую угадайку')


def is_valid(n):
    if n.isdigit() is True and 1 <= int(n) <= 100:
        return True
    else:
        return False


while True:
    n = input('Введите число от 1 до 100')
    if is_valid(n) is False:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    else:
        n = int(n)
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
