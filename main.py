from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config

import logging

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Название Python произошло от...'
    answers = [
        'от рептилии',
        'от ТВ-шоу «Летающий цирк Монти Пайтона»',
        'от ТВ-шоу «Вечер с Монти Пайтоном»',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        reply_markup=markup
    )


@dp.callback_query_handler(text='button_call_1')
async def quiz_2(call: types.callback_query):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('NEXT', callback_data='button_call_2')
    markup.add(button_call_2)

    question = 'В какой стране изобрели язык программирования Python'
    answers = [
        'Нидерланды',
        'Германия',
        'США',
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        reply_markup=markup
    )


@dp.message_handler(commands=['mem'])
async def photo_1(message: types.Message):
    photo = open('media/mem_1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await bot.send_message(message.from_user.id, int(message.text)**2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)







