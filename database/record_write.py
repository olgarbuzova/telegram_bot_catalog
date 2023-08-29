from datetime import datetime
from database.models import History
from config_data.config import CUSTOM_COMMANDS, CATEGORY


def record_write(user_id: int, user_name: str, data: dict) -> None:
    """Функция создает запись в таблице в базе данных"""
    text = "{0} ({1}шт)\n{2}".format(CATEGORY.get(
        data["category"]), data["quantity_of_goods"], CUSTOM_COMMANDS.get(data["command"]))
    if data.get("cost_from") is not None:
        text += "от {0} до {1}".format(data["cost_from"], data["cost_to"])
    new_record = History(user_id=user_id, user_name=user_name,
                         request=text, created_at=datetime.now())
    new_record.save()
