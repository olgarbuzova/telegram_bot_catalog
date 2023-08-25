

def set_params(command: str, limit: str, *args) -> dict:
    """Функция формирует словарь с параметрами для 
    аргумента params метода get библиотеки requests"""
    payload = {}
    if command == "low":
        payload["order"] = "price:asc"
    elif command == "high":
        payload["order"] = "price:desc"
    elif command == "custom":
        price_from = args[0]
        price_to = args[1]
        payload["price[from]"] = price_from
        payload["price[to]"] = price_to
    payload["limit"] = limit
    return payload
