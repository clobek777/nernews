import mysql.connector
from mysql.connector import errorcode
from mysql_cfg import get_creds_mysql
from json_test import load_json_file
from json_test import clean_text

user, password, host, database = get_creds_mysql()
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




mycursor = cnx.cursor()
sql = "INSERT INTO messages (tg_id, plain_text) VALUES (%s, %s);"
val = load_json_file('data/data.json', 1)
mycursor.executemany(sql, val)

cnx.commit()

print(mycursor.rowcount, "record inserted.")
cnx.close()