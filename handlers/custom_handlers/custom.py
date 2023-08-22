from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["custom"])
def bot_low(message: Message):
    bot.send_message(message.chat.id, "Список товаров в диапазоне цен")
