from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    """Функция создает макет для построения кнопок"""
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


button_list = [
    InlineKeyboardButton("Холодильники", callback_data="refrigerator"),
    InlineKeyboardButton("Посудомоечные машины", callback_data="dishwasher"),
    InlineKeyboardButton("Стиральные машины", callback_data="washingmachine")
]

reply_markup_first = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
