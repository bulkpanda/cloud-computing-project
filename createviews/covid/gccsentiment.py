import logging
import couchdb
dbname='tweetscovid'
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
  if(doc.region_code){
    var sentiment = 'neutral';
    if(doc.sentiment>0.1){
      sentiment='positive';
    }
    else if(doc.sentiment<-0.1) {
      sentiment='negative';
    }
    emit([doc.region_code, sentiment], 1);
  }
}'''
createView( db, "gccsentiment", "new-view", mapFunction )
