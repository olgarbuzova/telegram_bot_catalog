from telebot.types import Message
from loguru import logger
from loader import bot
from database.models import History


@bot.message_handler(commands=["history"])
def bot_history(message: Message):
    """Функция запускает команду /history"""
    logger.info("Пользователем запрошена команда /history")
    user_id = message.from_user.id
    history_list = History.select().where(
        History.user_id == user_id).order_by(-History.created_at).limit(10)
    bot.send_message(
        message.chat.id, "Вот последние ваши запросы")
    for item in history_list:
        bot.send_message(message.chat.id, item.request)
