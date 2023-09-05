import sqlite3 as sq
from config_data import config

def create_table():
    """
    Создает базу данных если её еще нет, таблицу с данными пользователей:
    id, username и, если есть, "имя фамилия" и добавляет туда данные, если
    бота запускает новый пользователь. Данная таблица не участвует в выдаче сохраненной
    информации. Она просто хранит данные пользователя.
      """
    connection = sq.connect(config.DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        chat_id INTEGER UNIQUE,
        username STRING,
        full_name TEXT
    );
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS query(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id INTEGER,
        date_time STRING,
        input_city STRING,
        destination_id STRING,
        photo_need STRING,
        response_id INTEGER,
        FOREIGN KEY (response_id) REFERENCES response(id) ON DELETE CASCADE ON UPDATE CASCADE
    );
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS response(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            query_id INTEGER,
            hotel_id STRING,
            name STRING,
            address STRING,
            price REAL,
            distance REAL,
            FOREIGN KEY (hotel_id) REFERENCES images(hotel_id) ON DELETE CASCADE ON UPDATE CASCADE
        );
        """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS images(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                hotel_id INTEGER REFERENCES response (id),
                link TEXT
                );""")

