import logging
import couchdb
dbname='mastodon_toots'
dbaddress='http://admin:Royai99@172.26.131.200/'
couch=couchdb.Server(dbaddress)
db=couch[dbname]

def createView( dbConn, designDoc, viewName, mapFunction ):
    data = {
            "_id": f"_design/{designDoc}",
            "views": {
                viewName: {
                    "map": mapFunction,
                    "reduce":"_count"
                    }
            },
            "language": "javascript",
            "options": {"partitioned": False }
            }
    logging.info( f"creating view {designDoc}/{viewName}" )
    dbConn.save( data )

mapFunction = '''function (doc) {
  if(doc.date){
    var date=doc.date.split(' ')[0];
    var neg=doc.sentiment.neg;
    var neu=doc.sentiment.neu;
    var pos=doc.sentiment.pos;
    var sentiment='neutral';
    if(neg>neu && neg>pos){
         sentiment='negative';
    }
    if(pos>neg && pos>neu){
         sentiment='positive';
    }
    if(neu>pos && neu>neg){
        sentiment='neutral';
    }
    emit([date, sentiment],1);
  
  }
}'''
createView( db, "datesentiment", "new-view", mapFunction )