from telebot.types import Message
from loguru import logger

from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    """Функция отправляет сообщение на команду /start"""
    bot.reply_to(
        message, f"Добро пожаловать, {message.from_user.full_name}!")
    logger.info(
        f"Пользователь {message.from_user.id} - {message.from_user.username} начал чат с ботом")
