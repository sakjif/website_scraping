from peewee import *
from decouple import config
from parse_logic import parsed_data


parsing_data_db = PostgresqlDatabase(
    config('DB_NAME'), user=config('DB_USER'), password=config('DB_PASSWORD'), host=config('DB_HOST')
)


class ParseData(Model):
    """Parse data model"""

    image = TextField()
    title = TextField()
    location = CharField()
    date_posted = CharField()
    bedroom = CharField()
    description = TextField()
    price = CharField()
    currency = CharField()

    class Meta:
        database = parsing_data_db


parsing_data_db.connect()
parsing_data_db.init(config('DB_NAME'), user=config('DB_USER'), password=config('DB_PASSWORD'), host=config('DB_HOST'))
parsing_data_db.create_tables([ParseData])
print("[INFO] Table created successfully")


def insert_data(data):
    with parsing_data_db.atomic():
        ParseData.insert_many(data).execute()
    print("[INFO] Data was successfully inserted")


parsing_data_db.close()

insert_data(parsed_data)
