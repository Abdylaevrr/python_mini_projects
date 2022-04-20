type = input('Choose a type (e - encryption, d - description): ')
language = input('Choose language (ru - russian, en- english: ')
shift_step = int(input('Choose shift step: '))
text = input('Enter text you want to encrypt or descript: ')


def cesar(text, type, lang, step):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    result = ''
    if type == 'd':
        if lang == 'ru':
            for i in range(len(text)):
                if text[i].isupper():
                    x = (rus_upper_alphabet.find(text[i]) - step) % 32
                    result += rus_upper_alphabet[x]
                elif text[i].islower():
                    x = (rus_lower_alphabet.find(text[i]) - step) % 32
                    result += rus_lower_alphabet[x]
                else:
                    result += text[i]
        elif lang == 'en':
            for i in range(len(text)):
                if text[i].isupper():
                    x = (eng_upper_alphabet.find(text[i]) - step) % 26
                    result += eng_upper_alphabet[x]
                elif text[i].islower():
                    x = (eng_lower_alphabet.find(text[i]) - step) % 26
                    result += eng_lower_alphabet[x]
                else:
                    result += text[i]
    elif type == 'e':
        if lang == 'ru':
            for i in range(len(text)):
                if text[i].isupper():
                    x = (rus_upper_alphabet.find(text[i]) + step) % 32
                    result += rus_upper_alphabet[x]
                elif text[i].islower():
                    x = (rus_lower_alphabet.find(text[i]) + step) % 32
                    result += rus_lower_alphabet[x]
                else:
                    result += text[i]
        elif lang == 'en':
            for i in range(len(text)):
                if text[i].isupper():
                    x = (eng_upper_alphabet.find(text[i]) + step) % 26
                    result += eng_upper_alphabet[x]
                elif text[i].islower():
                    x = (eng_lower_alphabet.find(text[i]) + step) % 26
                    result += eng_lower_alphabet[x]
                else:
                    result += text[i]
    return result


print(cesar(text, type, language, shift_step))
