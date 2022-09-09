import psycopg2
from decouple import config
from parse_logic import parsed_data


def insert_data(data):
    """Insert parsed data into DB"""
    try:
        # Connect to the DB
        connection = psycopg2.connect(
            dbname=config('DB_NAME'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            port=config('DB_PORT', cast=int),
            host=config('DB_HOST')
        )
        connection.autocommit = True

        # Create Table
        with connection.cursor() as cursor:
            cursor.execute(
                f"""CREATE TABLE {config('DB_TABLE')}(
                    id serial PRIMARY KEY,
                    image text,
                    title text,
                    date_posted varchar(255),
                    location varchar(255),
                    bedroom varchar(255),
                    description text,
                    currency varchar(255),
                    price varchar(255));"""
            )
            print("[INFO] Table created successfully")

        # Insert data into Table
        with connection.cursor() as cursor:
            data_value = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s)", x).decode('utf-8') for x in data)

            cursor.execute(
                f"Insert into {config('DB_TABLE')}"
                f"(image, title, location, date_posted, bedroom, description, price, currency) values " + data_value
            )
            print("[INFO] Data was successfully inserted")

    except Exception as exception:
        print("[INFO] Error while working with PostgreSQL", exception)


insert_data(parsed_data)
