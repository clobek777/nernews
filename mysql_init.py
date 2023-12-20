import mysql.connector
from mysql.connector import errorcode
from mysql_cfg import get_creds_mysql

user, password, host, database = get_creds_mysql()

def mysql_init():
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
    return (mycursor)