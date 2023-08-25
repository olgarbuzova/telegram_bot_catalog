import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")

URL = "https://catalog.onliner.by/sdapi/catalog.api/search/"

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("product_selection", "Выбрать товар")
)
CUSTOM_COMMANDS = {"low": "Список товаров по минимальной цене",
                   "high": "Список товаров по максимальной цене",
                   "custom": "Список товаров в диапазоне цен"}

CATEGORY = {"refrigerator": "Холодильники",
            "dishwasher": "Посудомоечные машины",
            "washingmachine": "Стиральные машины"}
