from telethon import TelegramClient, events, sync
import json
import time
#from nltk.tokenize import sent_tokenize
from telegram import get_creds
from check_id import get_tg_id
from mysql_init import mysql_init
import mysql.connector
from mysql.connector import errorcode
from mysql_cfg import get_creds_mysql
# Remember to use your own values from my.telegram.org!
api_id, api_hash = get_creds()
user, password, host, database = get_creds_mysql()

client = TelegramClient('mysession', api_id, api_hash)

try:
    cnx = mysql.connector.connect(user=user, password=password,
                                  host=host,
                                  database=database,
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

client.start()
channel_name = 'shadow_policy'
#channel_name = 'rospres'
last_tg_id = int(get_tg_id())
print(last_tg_id)
bulk = list()

# Preprocess message before saving it

ch_entity = client.get_entity("telegram.me/shadow_policy")
#for message in client.iter_messages(channel_name, reverse=True):
for message in client.iter_messages(ch_entity,min_id=last_tg_id, reverse=True):
    if message.text == '':
        continue

#    msg_list = process_message(message.text)

    #print(message.text)
    r = (message.id, message.text)
    print(r)
    bulk.append(r)
    mycursor.execute(sql, (int(message.id), message.text))
    cnx.commit()

    time.sleep(1)


filename = "data/data_last_tg_id_test.json"
#filename = "data/" + ch_entity.title + ".json"
with open(filename, 'w', encoding='utf-8') as json_file:
    json.dump(bulk, json_file, ensure_ascii=False)
