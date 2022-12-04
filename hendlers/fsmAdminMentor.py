from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from database.bot_db import sql_command_insert

class FSMAdmin(StatesGroup):
    mentor_id = State()
    name = State()
    age = State()
    napravlenie = State()
    crew = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.mentor_id.set()
        await message.answer('Напишите ваш ID')
    else:
        await message.answer('Напишите в личку')

async def load_mentor_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mentor_id'] = message.from_user.id
    await FSMAdmin.next()
    await message.answer('Укажите ваше имя.')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = f'@{message.from_user.username}'
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Укажите возраст.')


async def load_age(message: types.Message, state: FSMContext):
    try:
        if  16 < int(message.text) < 70:
            async with state.proxy() as data:
                data['age'] = int(message.text)
            await FSMAdmin.next()
            await message.answer('Укажите направление.')
        else:
            await message.answer('Нет доступа')
    except:
        await message.answer('Укажите правильно возраст')


async def load_napravlenie(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['napravlenie'] = message.text
    await FSMAdmin.next()
    await message.answer('Укажите группу')

async def load_crew(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['crew'] = message.text

        await bot.send_message(message.from_user.id,
                               f"{data['mentor_id']}\n{data['name']}\n{data['age']})"
                               f"{data['napravlenie']}\n{data['crew']}")
    await FSMAdmin.next()
    await message.answer('Всё верно?')

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await sql_command_insert(state)
        await state.finish()
        await message.answer('Регистрация окончена')
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Отмена')

    else:
        await message.answer('Введите правильное слово')

def register_hendlers_fsmAdminMentor(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_mentor_id, state=FSMAdmin.mentor_id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_napravlenie, state=FSMAdmin.napravlenie)
    dp.register_message_handler(load_crew, state=FSMAdmin.crew)
    dp.register_message_handler(submit, state=FSMAdmin.submit)