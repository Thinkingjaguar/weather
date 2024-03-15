from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from base import add_user, delete_user
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboard import get_city
from parser import get_weather

router = Router()


class Registration(StatesGroup):
    choosed_city = State()


@router.message(Command('start'), StateFilter(None))
async def start_reg(message: types.Message):
    await message.answer(text='Выберите Ваш город:', reply_markup=get_city())


@router.message(Command('relogin'), StateFilter(None))
async def no(message: types.Message):
    await message.answer('Вы и так не зарегистрированы.')


@router.message(Command('relogin'), Registration.choosed_city)
async def yes(message: types.Message, state: FSMContext):
    delete_user(message.from_user.id)
    await message.answer('Вы успешно удалены')
    await state.clear()


@router.callback_query(F.data[:4] == 'city')
async def add_new_user(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    add_user(callback.from_user.id, callback.data[5:])
    await state.set_state(Registration.choosed_city)
    await callback.message.answer(f'Температура сегодня{get_weather(callback.data[6:])}')
    await callback.answer()