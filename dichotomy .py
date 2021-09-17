from math import *

class dichotomy:
    
    def __init__(self, a, b, epsilon, function):
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.function = function
        
    def evaluation(self, x):
        return eval(self.function)

dichotomy_object = dichotomy(float(input('Введите левую границу ')), float(input('Введите правую границу ')), float(input('введите величину погрешности ')), input('Введите уравнение '))

assert dichotomy_object.b > dichotomy_object.a, 'Правая граница должна быть больше левой!'

def function(x):
    return dichotomy_object.evaluation(x)

while abs(dichotomy_object.b - dichotomy_object.a) > dichotomy_object.epsilon:
    result = (dichotomy_object.a + dichotomy_object.b) / 2
    if function(result) == 0:
        break
    elif function(dichotomy_object.a) * function(result) < 0:
        dichotomy_object.b = result
    elif function(dichotomy_object.b) * function(result) < 0:
        dichotomy_object.a = result
        
print('Корень уравнения f(x) = ' + dichotomy_object.function + ' равен', result, 'с погрешностью', dichotomy_object.epsilon)