# Задача 1. Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
def step(a, b):
    if b == 0:
        return 1
    else:
        return a * step(a, b - 1)
print(step(a, b))

# Задача 2. Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
def sum(a, b):
    if a == 0:
        return(b)
    if b == 0:
        return(a)
    else:
        return sum(a - 1, b + 1)
print(sum(a, b))