from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

with open("teg_api") as file:
    api = file.read()

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
kb.add(button_1)
kb.add(button_2)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(text='Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    # 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161
    norma_calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) - 161
    await message.answer(f'Ваша норма калорий: {norma_calories}')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
