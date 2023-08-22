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
    InlineKeyboardButton("Минимальная цена", callback_data="low"),
    InlineKeyboardButton("Максимальная цена", callback_data="high"),
    InlineKeyboardButton("Указать диапазон цен", callback_data="custom"),
    InlineKeyboardButton("Назад", callback_data="back")
]

reply_markup_second = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
