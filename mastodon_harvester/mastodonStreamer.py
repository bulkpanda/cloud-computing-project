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

from mastodon import Mastodon, MastodonError, StreamListener
import csv, os, time, json, sys
import couchdb
from tootProcessor import TootProcessor
import configparser


config = configparser.ConfigParser()
config.read("config.ini")
couch_IPs = eval(config['couchDB']['server_ips'])
dbname = config['couchDB']['dbname']

couch = None

for ip in couch_IPs:
    try:
        couch = couchdb.Server(ip)
    except Exception as e:
        print(e)
    else:
        break

if couch is None:
    print("Unable to connect to couchDB")
    exit()

if dbname in couch:
    db=couch[dbname]
else:
    db=couch.create(dbname)

MASTODON_ACCESS_TOKEN=sys.argv[2]
base_url=sys.argv[1]


m = Mastodon(
        api_base_url=base_url,
        access_token=MASTODON_ACCESS_TOKEN
    )

processor = TootProcessor()

class Listener(StreamListener):
    def on_update(self, status):

        # print(json.dumps(status, indent=2, sort_keys=True, default=str))
        toot_id, data = processor.processToot(status, base_url)
        if toot_id == None:
            return
        
        print(data)
        print(toot_id)

        # save to the couchdb server
        db[toot_id] = data



try:
    m.stream_public(Listener())
except MastodonError as e:
    print(e)