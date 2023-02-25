# Задача 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

a = set()
b = set()
n = int(input())
m = int(input())
for i in range(n):
    a.add(int(input()))
print(a)
for i in range(m):
    b.add(int(input()))
print(b)
if len(a) > len(b):
    p = a.intersection(b)
    print(p)
else:
    p = b.intersection(a)
    print(p)


#Задача 2. 

n = int(input('Число кустов: '))
a = []
for i in range(n):
    x = int(input('Количество ягод: '))
    a.append(x)
    print(a)
num = int(input('Номер куста: '))
for i in range(len(a) - 1):
    num = (a[i - 1] + a[i] + a[i + 1])
num = (a[-2] + a[-1] + a[0])
print(max(a))
