from telebot.handler_backends import State, StatesGroup


class Menu(StatesGroup):
    category = State()
    command = State()
    quantity_of_goods = State()
    cost_from = State()
    cost_to = State()
