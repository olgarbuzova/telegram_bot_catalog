
# Telegram-бот для получения информации о товарах с сайта catalog.onliner.by
Cкрипт - Python 3.
Библиотека для создания бота  [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

## Как создать и настроить этот бот
1. Обратись к @BotFather для получения токена
2. Определите переменные окружения в .env. Пример переменных окружения находится в файле .env.trmplate

## Запуск бота:
Запустить файл main.py

## Переменные среды
Переменные среды находятся в файле requirements.txt. Для установки необходимо выполнить:
```
$ pip install -r requirements.txt
```

## Добавление нового функционала
1. Команды бота находятся в пакете handlers. Основные системные команды: /start, /help и /echo находятся в пакете default_handlers. Для команд, выполняющих определенные задачи есть пакет custom_handlers.
Чтобы команда отображалась в меню бота следует прописать ее в переменную DEFAULT_COMMANDS в файл config.py.
2. Клавиатуры бота находятся в пакете keyboards. Это встроенные клавиатуры InlineKeyboardButton.

## Взаимодействие с базой данных
Модели распологаются в пакете database в файле models.py. В этом же пакете хранятся функции.

## API стороннего сервиса
Запросы к сайту catalog.onliner.by находятся в пакете API, там же можно найти и вспомогательные функции, касающиеся запросов.

## Логирование
Запись логов осуществляется в файл logs.log.
Изменить настройки для записи логов можно в файле loader.py





