from telethon import TelegramClient, events, sync
import json
import time
#from nltk.tokenize import sent_tokenize
from telegram import get_creds
from check_id import get_tg_id
# Remember to use your own values from my.telegram.org!
api_id, api_hash = get_creds()

client = TelegramClient('anon', api_id, api_hash)

client.start()
channel_name = 'shadow_policy'
#channel_name = 'rospres'
last_tg_id = get_tg_id()
bulk = list()

# Preprocess message before saving it
def process_message(plain_message):
    """
    Returns tokenized version of a message

    :param message: text to split into sentences
    """
    msg_list = sent_tokenize(plain_message, language="russian")

    #return msg_list
    return plain_message

ch_entity = client.get_entity("telegram.me/shadow_policy")
#for message in client.iter_messages(channel_name, reverse=True):
for message in client.iter_messages(ch_entity, reverse=True):
    if message.text == None:
        continue

#    msg_list = process_message(message.text)

    #print(message.text)
    r = (message.id, message.text)
    if int(message.id) >= int(last_tg_id):
        print(r)
        bulk.append(r)

    # Debug printing
    #if len(msg_list) != 0:
        #print("id:{} msg:{}".format(message.id, msg_list[0]))
     #   print("id:{} msg:{}".format(message.id, msg_list))

    # Check if there is a photo or video
  #  if message.media is not None:
        #output = "data/{}/{}".format(channel_name, message.id)
   #     output = "data/{}/{}".format(ch_entity.title, message.id)
    #    client.download_media(message=message, file=output)

    if message.id >= 1000:
        print("---------------------- I've reached the limit! ____________________\n")
        # Exit for debug
        # break

    time.sleep(1)
filename = "data/data_last_tg_id_test.json"
#filename = "data/" + ch_entity.title + ".json"
with open(filename, 'w', encoding='utf-8') as json_file:
    json.dump(bulk, json_file, ensure_ascii=False)


'''
for message in client.get_messages(channel_name, limit=5):
    msg_list = process_message(message.message)
    print(msg_list[0])
'''

'''
@client.on(events.NewMessage(chats='shadow_policy'))
async def my_event_handler(event):
    print(event.raw_text)

client.start()
client.run_until_disconnected()
'''
