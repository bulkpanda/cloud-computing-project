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
                    "reduce":"_stats"
                    }
            },
            "language": "javascript",
            "options": {"partitioned": False }
            }
    logging.info( f"creating view {designDoc}/{viewName}" )
    dbConn.save( data )

mapFunction = '''function (doc) {
  if(doc.place.full_name){
    var date=doc.time.split('T');
    emit([date[0], doc.place.full_name], doc.sentiment);
  }
}'''
createView( db, "dateplace-sentiment", "new-view", mapFunction )