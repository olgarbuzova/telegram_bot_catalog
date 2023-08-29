from telebot.types import Message
from loader import bot
from keyboards.inline.start_menu import reply_markup_first
from keyboards.inline.commands_menu import reply_markup_second
from states.menu_state import Menu
from config_data.config import CUSTOM_COMMANDS, CATEGORY
from API.api_handlers import get_list_of_goods, send_info
from API.set_params import set_params
from database.record_write import record_write


@bot.message_handler(commands=["product_selection"])
def product_selections(message: Message) -> None:
    """Функция запускает начало опроса, для выбора категории товаров"""
    bot.set_state(message.from_user.id, Menu.category, message.chat.id)
    bot.send_message(
        message.chat.id, "Какой товар будем искать?", reply_markup=reply_markup_first)


@bot.callback_query_handler(state=Menu.category, func=lambda call: True)
def callback_query_category(call) -> None:
    """Функция принимает ответ от клавиатуры start_menu, сохраняет состояние пользователя и
    предлогает выбрать следующие действие на клавиатуре commands_menu"""
    if call.data in ("refrigerator", "dishwasher", "washingmachine"):
        bot.send_message(chat_id=call.message.chat.id,
                         text=f"Выбрали {CATEGORY.get(call.data)}. В каком виде показывать?", reply_markup=reply_markup_second)
        bot.set_state(call.from_user.id,
                      Menu.command, call.message.chat.id)
        with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            data["category"] = call.data


@bot.callback_query_handler(state=Menu.command, func=lambda call: True)
def callback_query_command(call) -> None:
    """Функция принимает ответ от клавиатуры commands_menu, в зависимости от ответа сохраняет
    нужное состояние пользователя и отправляет вопрос пользователю"""
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
def get_quantity_of_goods(message: Message) -> None:
    """Функция сохраняет состояние пользователя и отправляет пользователю
    сообщение с информацией о его выборе"""
    if message.text.isdigit():
        if int(message.text) > 10:
            message.text = "10"
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["quantity_of_goods"] = message.text
            if data["command"] in ("low", "high"):
                text = "Будем смотреть {0}\n{1}\nПокажу {2} шт".format(
                    CATEGORY.get(data["category"]), CUSTOM_COMMANDS.get(data["command"]), data["quantity_of_goods"])
                record_write(message.from_user.id,
                             message.from_user.username, data)
                bot.send_message(message.from_user.id, text)
                payload = set_params(
                    data["command"], data["quantity_of_goods"])
                list_of_goods = get_list_of_goods(data["category"], payload)
                send_info(list_of_goods, message)

            elif data["command"] == "custom":
                text = "Будем смотреть {0}\nЦена от {1} до {2}\nПокажу {3} шт".format(
                    CATEGORY.get(data["category"]), data["cost_from"], data["cost_to"], data["quantity_of_goods"])
                record_write(message.from_user.id,
                             message.from_user.username, data)
                bot.send_message(message.from_user.id, text)
                payload = set_params(
                    data["command"], data["quantity_of_goods"], data["cost_from"], data["cost_to"])
                list_of_goods = get_list_of_goods(data["category"], payload)
                send_info(list_of_goods, message)
        bot.delete_state(user_id=message.from_user.id,
                         chat_id=message.chat.id)

    else:
        bot.send_message(message.from_user.id,
                         "Колличество показываемых товаров должно быть числом")


@bot.message_handler(state=Menu.cost_from)
def get_cost_from(message: Message) -> None:
    """Функция сохраняет состояние пользователя и отправляет пользователю вопрос"""
    if message.text.isdigit():
        bot.send_message(message.from_user.id, "Введите цену до")
        bot.set_state(message.from_user.id, Menu.cost_to, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["cost_from"] = message.text
    else:
        bot.send_message(message.from_user.id,
                         "Цена должна быть числом")


@bot.message_handler(state=Menu.cost_to)
def get_cost_to(message: Message) -> None:
    """Функция сохраняет состояние пользователя и отправляет пользователю вопрос"""
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
