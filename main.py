from aiogram import executor
from config import dp
import logging
from hendlers import client, callback, extra, fsmAdminMentor

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMentor.register_hendlers_fsmAdminMentor(dp)

extra.register_handlers_extra(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)







