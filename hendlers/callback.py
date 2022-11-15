
from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot


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

@dp.callback_query_handler(text='button_call_2')
async def quiz_3(call: types.callback_query):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton('NEXT', callback_data='button_call_3')
    markup.add(button_call_3)

    question = 'В каком году изобрели язык программирования Python'
    answers = [
        '1988',
        '1985',
        '1989',
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        reply_markup=markup
    )


def register_handlers_callback(dp: Dispatcher):
    dp.callback_query_handler(quiz_2, text='button_call_1')
    dp.callback_query_handler(quiz_3, text='button_call_2')