# Задача 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
'''
n = int(input('Input number of coins: '))
resh = 0 
orl = 0
i = 0
while i < n:
    x = input('Which side is the coin : ')
    if x == 'resh':
        resh += 1
    else:
        orl += 1
    i += 1

if resh == orl or resh > orl:
    print('Minimum number of coins to be flipped is:', orl)
else:
    print('Minimum number of coins to be flipped is:', resh)


# Задача 2. Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input('Input the sum of the desired numbers:'))
p = int(input('Input the product of the desired numbers:'))

for x in range (1001):
    for y in range (1001):
        if x + y == s and x * y == p:
            print('Desired numbers is', x, 'and', y)


# Задача 3. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Input the number: '))
st = 1
x = 2 ** st
while x <= n:
    print(x)
st += 1

n = int(input('Input the number: '))
i = 0

while 2 ** i <= n:
 
    print(2 ** i)
    i += 1
'''
n = int(input('Input the number: '))
i = 0
x = 2 ** i
while x <= n:
    print(x)
    i += 1









