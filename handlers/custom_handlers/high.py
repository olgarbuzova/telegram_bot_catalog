from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["high"])
def bot_low(message: Message):
    bot.send_message(message.chat.id, "Список товаров по максимальной цене")
