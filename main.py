import asyncio

from aiogram import executor
from config import dp
import logging
from hendlers import client, callback, extra, fsmAdminMentor, notification
from database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMentor.register_hendlers_fsmAdminMentor(dp)
notification.register_handlers_notification(dp)

extra.register_handlers_extra(dp)





if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


