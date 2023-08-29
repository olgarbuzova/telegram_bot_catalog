import peewee as pw

db = pw.SqliteDatabase("bot_database.db")


class BaseModel(pw.Model):
    """Базовый класс BaseModel, описывающий модели. Класс-родитель peewee.Model"""

    class Meta:
        database = db


class History(BaseModel):
    """
    Класс History. Класс-родитель BaseModel.

    Attributes:
        user_id (peewee.ntegerField): ID пользователя в Telegram
        user_name (peewee.CharField): username пользователя в Telegram
        request (peewee.CharField) : информация о запросе пользователя
        created_at (peewee.DateTimeField): время создания модели
    """
    user_id = pw.IntegerField()
    user_name = pw.CharField()
    request = pw.CharField()
    created_at = pw.DateTimeField()
