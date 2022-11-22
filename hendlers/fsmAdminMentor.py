from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMAdmin(StatesGroup):
    mentor_id = State()
    name = State()
    napravlenie = State()
    age = State()
    crew = State()

async def fsm_start(message: types.Message):
    if message.chat.type == "privet":
        await FSMAdmin.mentor_id.set()
        await message.answer('Напишите ваш ID')
    else:
        await message.answer('Напишите в личку')

# async def load_mentor_id(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         print(data)
#
#         data['mentor_id'] = message.text
#         print(data)


def register_hendlers_fsmAdminMentor(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    # dp.register_message_handler(load_mentor_id, state=FSMAdmin.mentor_id)
