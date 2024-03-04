from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboard import get_city
from base import add_user, delete_user


bot = Bot(token='')
dp = Dispatcher()


class Registration(StatesGroup):
    choosed_city = State()


@dp.message(Command('start'), StateFilter(None))
async def start_reg(message: types.Message):
    await message.answer(text='Выберите Ваш город:', reply_markup=get_city())


@dp.message(Command('relogin'), StateFilter(None))
async def no(message: types.Message):
    await message.answer('Вы и так не зарегистрированы')


@dp.callback_query(F.data[:4] == 'city')
async def get_weather(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    add_user(callback.from_user.id, callback.data[5:])
    await state.set_state(Registration.choosed_city)
    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
