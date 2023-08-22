from telebot.types import Message
from loader import bot
from keyboards.inline.start_menu import reply_markup_first
from keyboards.inline.commands_menu import reply_markup_second
from states.menu_state import Menu
from config_data.config import CUSTOM_COMMANDS, CATEGORY


@bot.message_handler(commands=["product_selection"])
def product_selections(message: Message):
    """Функция запускает начало опроса, для выбора категории товаров"""
    bot.set_state(message.from_user.id, Menu.category, message.chat.id)
    bot.send_message(
        message.chat.id, "Какой товар будем искать?", reply_markup=reply_markup_first)


@bot.callback_query_handler(state=Menu.category, func=lambda call: True)
def callback_query_category(call):
    if call.data in ("refrigerator", "dishwasher", "washingmachine"):
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Выбрали {CATEGORY.get(call.data)}. В каком виде показывать?", reply_markup=reply_markup_second)
        bot.set_state(call.from_user.id,
                      Menu.command, call.message.chat.id)
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            data["category"] = call.data


@bot.callback_query_handler(state=Menu.command, func=lambda call: True)
def callback_query_command(call):
    if call.data in ("low", "high"):
        bot.send_message(chat_id=call.message.chat.id,
                         text="Сколько товаров показывать?\n(можно не больше 10)")
        bot.set_state(call.from_user.id,
                      Menu.quantity_of_goods, call.message.chat.id)
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            data["command"] = call.data
    elif call.data == "custom":
        bot.send_message(call.message.chat.id, "Введите цену от")
        bot.set_state(call.from_user.id,
                      Menu.cost_from, call.message.chat.id)
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            data["command"] = call.data
    elif call.data == "back":
        bot.set_state(call.from_user.id, Menu.category, call.message.chat.id)
        bot.send_message(
            call.message.chat.id, "Какой товар будем искать?", reply_markup=reply_markup_first)


@bot.message_handler(state=Menu.quantity_of_goods)
def get_quantity_of_goods(message: Message):
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["quantity_of_goods"] = message.text
            if data["command"] in ("low", "high"):
                text = "Будем смотреть {0}\n{1}\nПокажу {2} шт".format(
                    CATEGORY.get(data["category"]), CUSTOM_COMMANDS.get(data["command"]), data["quantity_of_goods"])
                bot.send_message(message.from_user.id, text)
            elif data["command"] == "custom":
                text = "Будем смотреть {0}\nЦена от {1} до {2}/nПокажу {3} шт".format(
                    CATEGORY.get(data["category"]), data["cost_from"], data["cost_to"], data["quantity_of_goods"])
                bot.send_message(message.from_user.id, text)
    else:
        bot.send_message(message.from_user.id,
                         "Колличество показываемых товаров должно быть числом")


@bot.message_handler(state=Menu.cost_from)
def get_cost_from(message: Message):
    if message.text.isdigit():
        bot.send_message(message.from_user.id, "Введите цену до")
        bot.set_state(message.from_user.id, Menu.cost_to, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["cost_from"] = message.text
    else:
        bot.send_message(message.from_user.id,
                         "Цена должна быть числом")


@bot.message_handler(state=Menu.cost_to)
def get_cost_to(message: Message):
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["cost_to"] = message.text
            bot.send_message(chat_id=message.chat.id,
                             text="Сколько товаров показывать?\n(можно не больше 10)")
            bot.set_state(message.from_user.id,
                          Menu.quantity_of_goods, message.chat.id)
    else:
        bot.send_message(message.from_user.id,
                         "Цена должна быть числом")
