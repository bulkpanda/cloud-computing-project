## Adding JSON database to couchDB
import couchdb
import json
dbname='tweetdataforcc'
dbaddress='http://admin:Royai99@127.0.0.1:5984/'
couch = couchdb.Server(dbaddress)
db = couch['tweets']
jsonfile=open('C:/Users/Kunal Patel/D folder/_Master_data_science/Cluster and Cloud Computing/twitter-place-data.json','r', encoding='utf-8')

for row in jsonfile:
    # print(row[:-2])
    try:
        db_entry = json.loads(row[:-2])
    except:
        print(f'This row can\'t be converted: {row}, position:{jsonfile.tell()}')
    else:
        db.save(db_entry)
        pass