## Adding JSON database to couchDB
# Number of tweets in couchDB file=3236320
import couchdb
import json
keyterms=['covid', 'covid-19', 'coronavirus', 'covid-vaccine']
dbname='tweetscovid'
dbaddress='http://admin:Royai99@127.0.0.1:5984/' #change the address to the couchdb server
couch = couchdb.Server(dbaddress)
if dbname in couch:
    del couch[dbname]
    db=couch.create(dbname)
else:
    db=couch.create(dbname)
filename='twitter-place-data.json'
filename='C:/Users/Kunal Patel/D folder/_Master_data_science/Cluster and Cloud Computing/assignment 2/twitter-profane.json'
jsonfile=open(filename,'r', encoding='utf-8')
i=1
data_array=[]
for row in jsonfile:
        try:
            data = json.loads(row[:-2])
        except:
            print(f'This row can\'t be converted: {row}')
        else:
            tokens=data['tokens']
            tokenlist=tokens.split("|")
            for word in tokenlist:
                if word.lower() in keyterms:
                    data_array.append(data)
                    break
        if(len(data_array))==100:
             db.update(data_array)
             data_array=[]