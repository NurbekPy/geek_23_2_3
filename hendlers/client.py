from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot


#@dp.message_handler(commands=['quiz'])
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

#@dp.message_handler(commands=['mem'])
async def photo_1(message: types.Message):
    photo = open('media/mem_1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

async def pin_1(message: types.Message):
    if message.reply('!pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(photo_1, commands=['mem'])
    dp.register_message_handler(pin_1, commands=['!pin'])
