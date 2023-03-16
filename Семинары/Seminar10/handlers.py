import random
import config
from creat_bot import dp
from aiogram.types import Message



@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}, привет! Сегодня поиграем в игру. Если согласен, жми /new')


@dp.message_handler(commands=['new'])
async def mes_new_game(message: Message):
    config.total = 150
    await message.answer(text=f'Итак, на столе {config.total} конфет. Кидаем жребий, кто берет конфеты первым.')
    coin = random.randint(0, 1)
    if coin:
        await message.answer(text=f'{message.from_user.first_name}, поздравляю! Выпал орел. Ты ходишь первым. Бери от 1 до 28 конфет')
    else:
        await message.answer(text=f'{message.from_user.first_name}, не растраивайся. Первый ход делает бот')
        await bot_turn(message)

@dp.message_handler()
async def all_catch(message: Message):
    if message.text.isdigit():
        if 0 < int(message.text) < 29:
            await player_turn(message)
        else:
            await message.answer(text=f'Ах ты, хитрюга. Конфет нужно взять хотя бы одну, но не больше 28. Попробую еще раз. ')

    else:
        await message.answer(text=f'Введи цифрами число от 1до 28')


async def player_turn(message: Message):
    take_amount = int(message.text)
    config.total -= take_amount
    name = message.from_user.first_name
    await message.answer(text=f'{name} взял {take_amount} конфет. И на столе осталось {config.total} конфет.')
    if await check_victory(message, name):
        return
    await message.answer(text=f'{name}, передаем ход боту.')
    await bot_turn(message)

async def bot_turn(message: Message):
    take_amount = 0
    if config.total <= 28:
        take_amount = config.total
    else:
        take_amount = config.total%29 if config.total%29 != 0 else 1
    config.total -= take_amount
    name = message.from_user.first_name
    await message.answer(text=f'Бот взял {take_amount} конфет. На столе осталось {config.total} конфет')

    if await check_victory(message, 'Бот'):
        return
    await message.answer(text=f'{name}, теперь твой черед. Бери конфеты.')


async def check_victory(message: Message, name: str):
    if config.total <= 0:
        await message.answer(text=f'Победитель - {name}. Это была славная игра!')
        return True

    return False




