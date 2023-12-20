import mysql.connector
from mysql.connector import errorcode
from mysql_cfg import get_creds_mysql

user, password, host, database = get_creds_mysql()

def  get_tg_id():
    try:
        cnx = mysql.connector.connect(user = user, password = password,
                                      host = host,
                                      database = database,
                                      charset='utf8mb4')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        exit(-1)

    cursor = cnx.cursor()
    sql_last_id = "SELECT MAX(tg_id) FROM messages;"

    # Выполнение SQL-запроса
    cursor.execute(sql_last_id)

    # Получение результата
    last_tg_id = cursor.fetchone()[0]

    # Вывод последнего значения
    print(f"Последнее значение в столбце id: {last_tg_id}")

    # Закрытие курсора и соединения
    cursor.close()
    cnx.close()
    return (last_tg_id)


get_tg_id()