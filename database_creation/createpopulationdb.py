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
import json
import couchdb
dbname='populationdata'
dbaddress='http://admin:Royai99@127.0.0.1:5984/' #change the address to the couchdb server
couch = couchdb.Server(dbaddress)
if dbname in couch:
    del couch[dbname]
    db=couch.create(dbname)
else:
    db=couch.create(dbname)
filename="abs_personal_income_total_income_distribution_gccsa_2017_18-2203814467673960259.json"
jsonfile=open(filename,'r', encoding='utf-8')
data=json.load(jsonfile)
features=data['features']
# print(features)
for feature in features:
    # print(feature)
    income=feature['properties']
    income['gccsa_code']=income['gccsa_code'].lower()
    # print(income)
    db.save(income)