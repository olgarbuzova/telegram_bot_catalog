from telebot.types import Message

from loader import bot


@bot.message_handler(state=None)
def bot_echo(message: Message):
    """Функция отправляет сообщение на текстовые сообщения без указанного состояния"""
    bot.reply_to(
        message, "Введите команду из меню или нажмите кнопку.\n" f"Сообщение: {message.text}"
    )
