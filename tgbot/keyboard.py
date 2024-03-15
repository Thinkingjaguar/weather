from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_city():
    kb = InlineKeyboardBuilder()
    kb.button(text='Екатеринбург', callback_data='city_ekb')
    kb.button(text='Москва', callback_data='city_msk')
    kb.adjust(2)
    return kb.as_markup()
