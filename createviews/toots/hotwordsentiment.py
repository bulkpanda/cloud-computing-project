import logging
import couchdb
dbname='toots'
dbaddress='http://admin:Royai99@127.0.0.1:5984/'
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
  if(doc.hottokens){
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
    var hotwords=doc.hottokens;
    for(index=0; index<hotwords.length; index++){
        emit([hotwords[index], sentiment],1);
    }
  }
}'''
createView( db, "hotwordsentiment", "new-view", mapFunction )