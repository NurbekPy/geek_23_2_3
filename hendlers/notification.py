import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('OK')

async def ski_time():
    await bot.send_message(
        chat_id=chat_id,
        text='Настало время ехать на лыжи!'
    )

async def scheduler():
    aioschedule.every().saturday.at('08:00').do(ski_time)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'notify' in word.text)


