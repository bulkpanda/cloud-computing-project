## Adding JSON database to couchDB
# Number of tweets in couchDB file=3236320
import couchdb
import json
keyterms=['covid', 'covid-19', 'coronavirus', 'covid-vaccine', 'vaccines', 'vaccine']
dbname='tweetscovid'
dbaddress='http://admin:Royai99@127.0.0.1:5984/' #change the address to the couchdb server
couch = couchdb.Server(dbaddress)
if dbname in couch:
    del couch[dbname]
    db=couch.create(dbname)
else:
    db=couch.create(dbname)
filename='twitter-place-data.json'
filename='C:/Users/Kunal Patel/D folder/_Master_data_science/Cluster and Cloud Computing/twitter-place-data.json'
jsonfile=open(filename,'r', encoding='utf-8')
i=-1
for row in jsonfile:
    # i+=1
    # if(i%10==0):
        # print(row[:-2])
        try:
            data = json.loads(row[:-2])
        except:
            print(f'This row can\'t be converted: {row}')
        else:
            try:
                place=data['doc']['includes']['places'][0]
            except:
                place={'full_name':'Australia'}
            time=data['doc']['data']['created_at']
            text=data['doc']['data']['text']
            sentiment=data['doc']['data']['sentiment']
            # tags=data['doc']['data']['entities']['mentions']
            tokens=data['value']['tokens']
            tokenlist=tokens.split("|")
            for word in tokenlist:
                if word.lower() in keyterms:
                    db_entry={
                        'place':place,
                        'time':time,
                        'text':text,
                        'sentiment':sentiment,
                        'tokens':tokens
                    }
                    db.save(db_entry)