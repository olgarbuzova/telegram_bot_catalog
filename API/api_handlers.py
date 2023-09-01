import requests
import json
from loguru import logger
from telebot.types import Message
from loader import bot
from config_data.config import URL


@logger.catch
def get_list_of_goods(category: str, payload: dict):
    """Функция получает данные из API"""
    url = "{}/{}".format(URL, category)
    response = requests.get(url, params=payload, timeout=30)
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        return data


def send_info(data, message: Message):
    """Отправляет сообщение пользователю с результатаим
    его запроса"""
    for item in data["products"]:
        info = "{0}\n{1}\nЦена: {2} руб\n".format(
            item["extended_name"], item["description"], item["prices"]["price_min"]["amount"])
        bot.send_photo(message.chat.id, "https:" +
                       item["images"]["header"], caption=info)
