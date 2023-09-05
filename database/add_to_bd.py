import sqlite3 as sq
from loguru import logger
from config_data import config



def add_user(message):
    """
    Подключается к базе данных и добавляет туда данные:
    id, username и, если есть, "имя фамилия" и добавляет туда данные, если
    бота запускает новый пользователь. Данная таблица не участвует в выдаче сохраненной
    информации. Она просто хранит данные пользователя.
      """
    connection = sq.connect(config.DB_NAME)
    cursor = connection.cursor()
    connection.commit()
    try:
        cursor.execute(
            "INSERT INTO user (chat_id, username, full_name) VALUES (?, ?, ?)", (
                message.chat.id,
                message.from_user.username,
                message.from_user.full_name
            )
        )
        logger.info(f'Добавлен новый пользователь. User_id: {message.chat.id}')
        connection.commit()
    except sq.IntegrityError:
        logger.info(f'Данный пользователь уже существует. User_id: {message.chat.id}')
    finally:
        connection.close()


def add_query(query_data):
    """
    Подключается к таблице и добавляет туда данные,
    которые ввел пользователь для поиска
    : param query_data : dict
    : return : None
    """
    user_id = query_data['chat_id']
    connection = sq.connect(config.DB_NAME)
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO query(user_id, input_city, photo_need, destination_id, date_time) VALUES (?, ?, ?, ?, ?)",
            (
                user_id,
                query_data['input_city'],
                query_data['photo_need'],
                query_data['destination_id'],
                query_data['date_time']
            )
        )
        logger.info(f'В БД добавлен новый запрос. User_id: {user_id}')

        # Нам не нужно очень много записей историй поиска, поэтому для каждого пользователя
        # будем хранить только 5 последних записей, лишние - удалим.
        cursor.execute(f"""
                DELETE FROM query WHERE query.[date_time]=
                (SELECT MIN([date_time]) FROM query WHERE `user_id` = '{user_id}' )
                AND
                ((SELECT COUNT(*) FROM query WHERE `user_id` = '{user_id}' ) > 5 ) 
            """
                       )
        connection.commit()
    except sq.IntegrityError:
        logger.info(f'Запрос с такой датой и временем уже существует. User_id: {user_id}')
    finally:
        connection.close()


def add_response(search_result):
    """
    Подключается к таблице и добавляет туда данные,
    которые бот получил в результате запросов к серверу.
    : param search_result : dict
    : return : None
    """
    connection = sq.connect(config.DB_NAME)
    cursor = connection.cursor()
    for item in search_result.items():
        cursor.execute(f"SELECT `id` FROM query WHERE `date_time` = ?", (item[1]['date_time'],))
        query_id = cursor.fetchone()[0]
        cursor.execute(
            "INSERT INTO response(query_id, hotel_id, name, address, price, distance) VALUES (?, ?, ?, ?, ?, ?)",
            (
                query_id,
                item[0],
                item[1]['name'],
                item[1]['address'],
                item[1]['price'],
                item[1]['distance']
            )
        )
        logger.info(f'В БД добавлены данные отеля. User_id: {item[1]["user_id"]}')
        for link in item[1]['images']:
            cursor.execute("INSERT INTO images (hotel_id, link) VALUES (?, ?)", (item[0], link))
        logger.info(f'В БД добавлены ссылки на фотографии отеля. User_id: {item[1]["user_id"]}')
        connection.commit()
    connection.close()
