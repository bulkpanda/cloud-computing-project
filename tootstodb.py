## Toot processing
from nltk.stem import PorterStemmer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
import html2text
import spacy
import couchdb
from string import punctuation
nlp = spacy.load("en_core_web_sm")

#function to get hotwords
def get_hotwords(text):
    result = []
    pos_tag = ['PROPN', 'NOUN']  # removed 'ADJ' terms
    doc = nlp(text.lower()) 
    for token in doc:
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            result.append(token.text)
    return result

# start the database
dbname='toots'
dbaddress='http://admin:Royai99@127.0.0.1:5984/'
#dbaddress='http://admin:Royai99@172.26.134.130:5984/' #change the address to the couchdb server
couch = couchdb.Server(dbaddress)
if dbname in couch:
    del couch[dbname]
    db=couch.create(dbname)
else:
    db=couch.create(dbname)

# read the json file
f=open('tootexamples/onetoot.json','r',encoding='utf-8') 
x=json.load(f)  
print(x.keys())
# get the date and text
date=x['created_at']      
text=x['content']          
h = html2text.HTML2Text()
h.ignore_links = True
text=h.handle(text).strip("\n ")
# get the sentiment
sentiment = SentimentIntensityAnalyzer()
sentimentscore=sentiment.polarity_scores(text)
# get the hottokens
hottokens=get_hotwords(text)
ps=PorterStemmer()
hottokenstems=[]
print(hottokenstems)
for word in hottokens:
    hottokenstems.append(ps.stem(word))
hottokenstems=list(set(hottokenstems))
print(hottokenstems)
data={
    'date':date,
    'sentiment':sentimentscore,
    'hottokens':hottokenstems
}
# save to the couchdb server
db.save(data)