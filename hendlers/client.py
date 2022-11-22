from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot
from asyncio import sleep

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
    if message.reply_('!pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)


async def start_dice(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.full_name} , игра начинается!')
    await sleep(1)
    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(5)

    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(5)

    if bot_data > user_data:
        await bot.send_message(message.from_user.id, 'Ты проиграл!')
    elif bot_data < user_data:
        await bot.send_message(message.from_user.id, 'Ты победил!')
    else:
        await bot.send_message(message.from_user.id, 'Ничья!')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(photo_1, commands=['mem'])
    dp.register_message_handler(pin_1, commands=['!pin'])
    dp.register_message_handler(start_dice, commands=['start'])
