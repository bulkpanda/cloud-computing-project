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
  if(doc.date){
    var date=doc.date.split(' ')[0];
    var hotwords=doc.hottokens;
    for(index=0; index<hotwords.length; index++){
        emit([date, hotwords[index]],1);
    }
  }
}'''
createView( db, "datehotwords", "new-view", mapFunction )