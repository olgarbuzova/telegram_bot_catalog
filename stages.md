# Этапы реализации финальной работы "Python. Часть 2"

**Название бота: Catalog**
** Пользователь: @OnlinerCatalogBot**

## Этапы реализации:
1. Создать предварительную структуру проекта
2. Создать виртуальное окружение, .gitignore, зарегистрировать бот, .env
3. Написать команды (без работы с API):
- /low
- /high
- /custom
4. Написать модуль, отвечающий за состояниее пользователя
5. Подключить модуль из пункта 4 и кнопки
6. Написать модуль, отвечающий за работу с API  [сatalog.onliner](<https://catalog.onliner.by/>). Примеры endpoints:
- выбор товара <https://catalog.onliner.by/sdapi/catalog.api/search/refrigerator>
- самая высокая цена <https://catalog.onliner.by/sdapi/catalog.api/search/refrigerator?order=price:desc>
- самая низкая цена <https://catalog.onliner.by/sdapi/catalog.api/search/refrigerator?order=price:asc>
- диапазон цен <https://catalog.onliner.by/sdapi/catalog.api/search/refrigerator?price[from]=100.00&price[to]=500.00>
7. Подключить модуль из пункта 6 к командам из пункта 3
8. Написать модуль, отвечающий за работу с базой данных. База данных будет хранить информацию о запросах пользователя.
9. Написать команду /history
10. Подключить модуль с БД
11. Написать модуль, отвечающий за логированние

