# Python program to read
# json file
import re
import json

def clean_text(input_text):
    # Регулярное выражение для удаления всех символов, кроме русских и латинских знаков препинания
    cleaned_text = re.sub(r'[^\w\s,.!?;:()-а-яА-ЯёЁA-Za-z]', '', input_text)
    return cleaned_text

def json_pars(data_path):
	# Opening JSON file
	#f = open(data_path, encoding="utf8")
	f = open('data/data.json', encoding="utf8")

	# returns JSON object as
	# a dictionary
	data = json.load(f)

	# Iterating through the json
	# list
	news_data = []
	for i in data:
		if len(i) == 2:
			news_data.append((int(i[0]),clean_text(str(i[1]))))
	# Closing file
	f.close()
	return (news_data)