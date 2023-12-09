import mysql.connector
from mysql.connector import errorcode
from mysql_cfg import get_creds_mysql

user, password, host, database = get_creds_mysql()
try:
    cnx = mysql.connector.connect(user = user, password = password,
                                  host = host,
                                  database = database)
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
val = [
  (4, 'Lowstreet 4'),
  (5, 'Apple st 652'),
  (6, 'Mountain 21'),
  (7, 'Valley 345'),
  (8, 'Ocean blvd 2'),
  (9, 'Green Grass 1'),
  (10, 'Sky st 331'),
  (11, 'One way 98'),
  (12, 'Yellow Garden 2'),
  (13, 'Park Lane 38'),
  (14, 'Central st 954'),
  (15, 'Main Road 989'),
  (16, 'Sideway 1633')
]
mycursor.executemany(sql, val)

cnx.commit()

print(mycursor.rowcount, "record inserted.")
cnx.close()