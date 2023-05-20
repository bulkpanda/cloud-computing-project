import couchdb
import json
import time

filename='/home/ubuntu/tweetdata/twitter-profane.json'
jsonfile=open(filename,'r', encoding='utf-8')
dbname='tweetsprofane'
dbaddress='http://admin:Royai99@127.0.0.1:5984/'
couch = couchdb.Server(dbaddress)
if dbname in couch:
    del couch[dbname]
    db=couch.create(dbname)
else:
    db=couch.create(dbname)
i=-1
data_array=[]
for row in jsonfile:
    i+=1
    try:
        data = json.loads(row[:-2])
        
    except:
        print(f'This row can\'t be converted: {row}')
    else:
        data_array.append(data)
        
    if(len(data_array)==1000):
        print(i)
        db.update(data_array)
        data_array=[]

if len(data_array)!=0:
    db.update(data_array)
