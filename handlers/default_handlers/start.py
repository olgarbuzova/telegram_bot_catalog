from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    """Функция отправляет сообщение на команду /start"""
    bot.reply_to(
        message, f"Добро пожаловать, {message.from_user.full_name}!")
