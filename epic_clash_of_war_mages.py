from random import *

def cube():
    print(randint(1, 6))

def input_cube():
    n = int(input('введите количество кубиков. '))
    return n

def throw(n):
    for i in range(n):
        cube()

Flag = True
while Flag == True:
    n = input_cube()
    throw(n)
    answer = input('Бросить еще раз? Да/Нет?')
    answer = answer.lower()
    if answer == 'да':
        Flag = True
    elif answer == 'нет':
        Flag = False