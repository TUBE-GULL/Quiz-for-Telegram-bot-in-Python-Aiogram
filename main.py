import asyncio
from aiogram import Bot, Dispatcher
from log import my_logo 
from app.components.read_token import read_token
from app.components.working_db import QuizeDatabase
from app.root import router

async def main()-> None:
    TOKEN = await read_token()
    #  добываю Token (read_token)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Инициализируем базу данных и создаю таблицу 
    db = QuizeDatabase() # инициализируем обект базы данных
    await db.create_table() # создаст таблицу если ее нет 
    
    # Добовляю в запуск свое лого 
    my_logo.logo()
    
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__  == '__main__':
    asyncio.run(main())