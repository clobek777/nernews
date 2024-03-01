import json
import spacy
from spacy import displacy
from collections import Counter
import pandas as pd
pd.options.display.max_rows = 600
pd.options.display.max_colwidth = 400

filename = 'data/data.json'
nlp = spacy.load('ru_core_news_md')

with open(filename, encoding='utf-8') as json_file:
    data = json.load(json_file)

for (id, msg) in data:
    if len(msg) != 0:
      #  print("id:{} msg:{}".format(id, msg))
        doc=nlp(msg)

        # Print Named entities
        for ne in doc.ents:
            if ne.label_ == 'ORG':
                print(ne, ne.label_)

        # Print Part of speech
      #  for token in doc:
      #      print(token.lemma_, token.pos_)
