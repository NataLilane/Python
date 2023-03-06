
# Задача 1. Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# Вар 1.

a = 'В-голове-моей-опилки Да-да-да'
st = a.lower().split()
print(st)
list_s = []
vowels = list('аеёиоуыэюя')
for item in st:
    s = 0
    for let in item:
        if let in vowels:
            s += 1
    list_s.append(s)
print(list_s)
if len(set(list_s)) == 1:
        print('Парам пам-пам')
else:
        print('Пам парам')
# Вар 2

#a = 'В-голове-моей-опилки Да-да-да'
a = 'Пара-ра-рам рам-пам-папам па-ра-па-да'
st = a.lower().split()
print(st)
list_s = []
vowels = list('аеёиоуыэюя')
list_s = [sum(x in vowels for x in item) for item in st]
print(list_s)
if len(set(list_s)) == 1:
        print('Парам пам-пам')
else:
        print('Пам парам')

# Задача 2. Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 

# Чем руководствовалась:
columns = int(input('Введите число столбцов:'))
rows = int(input('Введите число строк: '))
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print((i * j), end=" ")
    print()

# Задача:

num_rows = int(input('Введите число строк: '))
num_columns = int(input('Введите число столбцов:'))

def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end=' ')
        print()
print_operation_table(lambda x, y: x * y,num_rows, num_columns)



