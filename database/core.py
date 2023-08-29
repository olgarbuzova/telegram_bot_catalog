from database.models import db, History


db.connect()
db.create_tables([History])
