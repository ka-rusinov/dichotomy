from random import *

def alphabet():
    digit = [c for c in '0123456789']
    low_let = [c for c in 'abcdefghijklmnopqrstuvwxyz']
    upp_let = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    punct = [c for c in '!#$%&*+-=?@^_']
    alpha = []
    
    s1 = input('Включить в пароль символы "0123456789"? Да/Нет?')
    s1 = s1.lower()
    if s1 == 'да':
        alpha.extend(digit)
        
    s2 = input('Включить в пароль символы "abcdefghijklmnopqrstuvwxyz"? Да/Нет?')
    s2 = s2.lower()
    if s2 == 'да':
        alpha.extend(low_let)
        
    s3 = input('Включить в пароль символы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? Да/Нет?')
    s3 = s3.lower()
    if s3 == 'да':
        alpha.extend(upp_let)
        
    s4 = input('Включить в пароль символы "!#$%&*+-=?@^_"? Да/Нет?')
    s4 = s4.lower()
    if s4 == 'да':
        alpha.extend(punct)

    s5 = list(input('Исключить какие-нибудь символы из пароля? Если "да", введите эти символы без пробелов. Если "нет", просто нажмите Enter'))
    if s5 != '':
        for c in s5:
            i = alpha.index(c)
            del alpha[i]
    return alpha

def input_n():
    n = int(input('Введите требуемое количество паролей. '))
    return n
def input_m():
    m = int(input('Введите требуемую длину паролей. '))
    return m

def generate_password(m, alpha):
    password = ''
    for i in range(m):
        c = choice(alpha)
        password += c
    return password

def generator():
    for i in range(n):
        print(generate_password(m, alpha))

print('Вас приветствует программа генерации паролей.')

n, m = input_n(), input_m()
alpha = alphabet()
Flag = True

while Flag == True:
    generator()
    print('Сгенерировать еще паролей или выйти из программы?')
    answer_1 = input('Сгенерировать/Выйти? ')
    answer_1 = answer_1.lower()
    if answer_1 == 'сгенерировать':
        n, m = input_n(), input_m()
        alpha = alphabet()
        Flag = True
        continue
    elif answer_1 == 'выйти':
        Flag = False