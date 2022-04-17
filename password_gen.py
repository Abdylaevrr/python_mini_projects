import random

DIGITS = '23456789'
LOWERCASE_LETTERS = 'abcdefghjkmnpqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
OTHER = 'il1Lo0O'

chars = ''

num_password = int(input('Количество паролей для генерации '))
password_length = int(input('Длина одного пароля '))
include_digits = input('Включать ли цифры 0123456789? (д - да, н - нет) ')
include_upper = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д - да, н - нет) ')
include_low = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д - да, н - нет) ')
include_sym = input('Включать ли символы !#$%&*+-=?@^_? (д - да, н - нет) ')
exclude_sym = input('Исключать ли неоднозначные символы il1Lo0O? (д - да, н - нет) ')


def generate_password(length, chars):
    return ''.join(random.sample(chars, length))


for _ in range(num_password):
    if include_digits.lower() == 'д':
        chars += DIGITS
    if include_upper.lower() == 'д':
        chars += UPPERCASE_LETTERS
    if include_low.lower() == 'д':
        chars += LOWERCASE_LETTERS
    if include_sym.lower() == 'д':
        chars += PUNCTUATION
    if exclude_sym.lower() == 'н':
        chars += OTHER
    print(generate_password(password_length, chars))
