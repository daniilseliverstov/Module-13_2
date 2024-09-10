import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

with open("teg_api") as file:
    api = file.read()

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_massage(massage):
    print('Привет! Я бот помогающий твоему здоровью.')
    await massage.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massage(massage):
    print('Введите команду /start, чтобы начать общение.')
    await massage.answer('Введите команду /start, чтобы начать общение.\n '
                         'Пока что нет других команд')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
