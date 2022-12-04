import sqlite3

def sql_create():
    global db, cursor
    db = sqlite3.connect('bot1.sqlite3')
    cursor = db.cursor()

    if db:
        print('База данных подключена')

    db.execute('CREATE TABLE IF NOT EXISTS mentors '
               '(mentor_id INTEGER PRIMARY KEY, name TEXT, '
               'age INTEGER, napravlenie TEXT, crew INTEGER)')
    db.commit()

штш

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO mentors VALUES'
                       '(?, ?, ?, ?, ?)', tuple(data.values()))
        db.commit()
