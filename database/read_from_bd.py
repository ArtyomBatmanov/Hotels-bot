import sqlite3 as sq
from loguru import logger
from config_data import config




def read_query(user):
    """
        Принимает id пользователя, делает запрос к базе данных, получает в ответ
        результаты запросов данного пользователя.
        : param user : int
        : return : list
    """
    logger.info(f'Читаем таблицу query. User_id: {user}')
    connect = sq.connect(config.DB_NAME)
    cursor = connect.cursor()
    try:
        cursor.execute("SELECT `id`, `date_time`, `input_city`, `photo_need` FROM query WHERE `user_id` = ?", (user,))
        records = cursor.fetchall()
        connect.close()
        return records
    except sq.OperationalError:
        logger.info(f"В базе данных пока нет таблицы с запросами. User_id: {user}")
        return []
    finally:
        connect.close()


def get_history_response(message):
    """
       Принимает id-запроса, обращается к базе данных и выдает данные которые нашел бот для
       пользователя по его запросам.
       : param query : str
       : return : dict
    """
    logger.info(f'Читаем таблицу response. User_id: {message.chat.id}')
    connect = sq.connect(config.DB_NAME)
    cursor = connect.cursor()
    try:
        cursor.execute("SELECT * FROM response WHERE `query_id` = ?", (message.text,))
        records = cursor.fetchall()
        history = {}
        for item in records:
            hotel_id = item[2]
            history[item[2]] = {'name': item[3], 'address': item[4], 'price': item[5], 'distance': item[6]}
            cursor.execute("SELECT * FROM images WHERE `hotel_id` = ?", (hotel_id, ))
            images = cursor.fetchall()
            links = []
            for link in images:
                links.append(link[2])
            history[item[2]]['images'] = links
        connect.close()
        return history
    except sq.OperationalError:
        logger.info(f"В базе данных пока нет таблицы с запросами. User_id: {message.chat.id}")
        return {}
    finally:
        connect.close()

