# Задача 1. Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
'''
# Вар.1
a = []
n = int(input('Введите число: '))
count = 0
for i in range(n):
    a.append(i + 1)
   
print(a)
к = int(input('Введите искомое число: '))
for j in range(len(a)):
    if к == a[j]:
        count += 1
print(count)
# Вар. 2
a = []
n = int(input('Введите число: '))
for i in range(n):
    x = int(input())
    a.append(x)
print(a)
count = 0
k = int(input('Введите искомое число: '))
for i in a:
    if i == k:
        count += 1
print(count)

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Вар 1.
a = []
n = int(input('Введите число: '))
for i in range(n):
    a.append(i + 1)

print(a)
x = int(input('Введите второе число: '))
if x > n:
    print(a.pop())
for j in range(len(a)):
    if x == a[j]:
        print('Максимально близкое число ', a[j])

# Вар 2.
a = []
n = int(input('Введите число элементов: '))
for i in range(n):
    a.append(int(input()))
    print(a)

x = int(input('Введите  число: '))

minraz = abs(x - a[0]) # функция модуль - [-2] = 2, [2] = 2
for j in range(len(a)):
    raz = abs(x - a[j])
    
    if raz < minraz:
        minraz = raz
        num = a[j]
print(minraz, 'и', num)

# Вар.3 - лучший
a = []
n = int(input('Введите число: '))
for i in range(n):
    x = int(input())
    a.append(x)
print(a)  
x = int(input('Введите  число: '))
num = a[0]
minraz = abs(x - a[0])
for i in range(1, len(a)):
    if minraz > abs(x - a[i]):
        minraz = abs(x - a[i])
        num = a[i]
print(num)






# Задача 3. В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.


еng = {1: 'A E I O U L N S T R ',
       2: 'D G ',
       3: 'B C M P ',
       4: 'F H V W Y ',
       5: 'K',
       8: 'J X ',
       10: 'Q Z '}

rus = {1: 'А В Е И Н О Р С Т ',
       2: 'Д К Л М П У ',
       3: 'Б Г Ё Ь Я ',
       4: 'Й Ы ',
       5: 'Ж З Х Ц Ч ',
       8: 'Ш Э Ю ',
       10: 'Ф Щ Ъ '}
b = input('Введите "еng", если будите использовать английскую раскладку и "rus", если будите использовать русскую раскладку: ')
a = input('Введите слово: ')
sum = 0
if b == 'eng':
    for i in a:
        for k, v in еng.items():
            if i in v:
                sum = sum + k
print(sum, 'очков')

if b == 'rus':
    for i in a:
        for k, v in rus.items():
            if i in v:
                sum = sum + k
print(sum, 'очков')

'''
еng = {1: 'A E I O U L N S T R ',
       2: 'D G ',
       3: 'B C M P ',
       4: 'F H V W Y ',
       5: 'K',
       8: 'J X ',
       10: 'Q Z '}

rus = {1: 'А В Е И Н О Р С Т ',
       2: 'Д К Л М П У ',
       3: 'Б Г Ё Ь Я ',
       4: 'Й Ы ',
       5: 'Ж З Х Ц Ч ',
       8: 'Ш Э Ю ',
       10: 'Ф Щ Ъ '}

a = input('Введите слово: ').upper() # переводим в верхний регистр
count = 0
for i in a:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in eng:
            if i in eng[j]:
                count = count + j
    else:
        for j in rus:
            if i in rus[j]:
                count = count + 1
print(count)





