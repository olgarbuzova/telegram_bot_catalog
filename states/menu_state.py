from telebot.handler_backends import State, StatesGroup


class Menu(StatesGroup):
    """Класс для реализации состояний пользователя
    в процессе выбора категории товоров"""
    category = State()
    command = State()
    quantity_of_goods = State()
    cost_from = State()
    cost_to = State()
