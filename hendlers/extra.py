from aiogram import Dispatcher, types
from config import dp, bot
import random

#@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await bot.send_message(message.from_user.id, int(message.text)**2)
    else:
        await bot.send_message(message.from_user.id, message.text)


    emo = [
        '🏀',
        '🎲',
        '🎰',
        '🎯',
        '🥅',
        '🎳',
    ]

    random_emo = random.choice(emo)

    if message.text.startswith('game'):
        await bot.send_dice(message.chat.id, emoji=random_emo)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo,)
