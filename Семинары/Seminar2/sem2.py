

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
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

#if resh > orl:
 #   print('Minimum number of coins to be flipped is:', orl)
else:
    print('Minimum number of coins to be flipped is:', resh)


