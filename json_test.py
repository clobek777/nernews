# Python program to read
# json file
import re
import json

def clean_text(input_text):
    # Регулярное выражение для удаления всех символов, кроме русских и латинских знаков препинания
    cleaned_text = re.sub(r'[^\w\sа-яА-ЯёЁA-Za-z]', '', input_text)
    return cleaned_text.replace('\n',' ')















def load_json_file(filename, last_tgid):
	# Opening JSON file
	f = open(filename, encoding="utf8")
	#f = open('data/data.json', encoding="utf8")

	# returns JSON object as
	# a dictionary
	data = json.load(f)

	# Iterating through the json
	# list
	news_data = []
	for i in data:
		if len(i) == 2:
			print(i[1])
			print('\n\n\n--------------------------------------------------------------')
			print(clean_text(str(i[1])))
			break
	# Closing file
	f.close()
	return (news_data)
load_json_file('data/data.json', 1)