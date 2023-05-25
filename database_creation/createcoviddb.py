"""
    Cluster and Cloud Computing 2023
    Assignment 2
    Team 46

    Kunal Patel : 1291822
    Mayank Yadav : 1403092
    Harsh Mangla : 1418017
    Sophie von Doussa : 1064884
    Maxson Stephen Mathew : 1428525

    City : Melbourne
"""
import couchdb
import json
keyterms=['covid', 'covid-19', 'coronavirus', 'covid-vaccine']
dbname='tweetscovid'                                            # get the database name
dbaddress='http://admin:Royai99@127.0.0.1:5984/' #change the address to the couchdb server
couch = couchdb.Server(dbaddress)
if dbname in couch:                                 # create a new database if older one exist
    del couch[dbname]
    db=couch.create(dbname)
else:
    db=couch.create(dbname)

 # file's whose data needs to be read
filename='/home/ubuntu/tweetdata/twitter-profane.json'

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
        if(len(data_array))==100:                   # creating database with covid tweets
             db.update(data_array)
             data_array=[]