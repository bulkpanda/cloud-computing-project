import logging
import couchdb
dbname='tweetsprofane'
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
  if(doc.place.full_name){
    var date=doc.time.split('T')[0];
    var prof=doc.profanity;
    var proftext='';
    if(prof>0.7){
      proftext='high';
    }
    if(prof<=0.7 && prof>0.4){
      proftext='mid';
    }
    if(prof<=0.4){
      proftext='low'
    }
    emit([date, doc.place.full_name, proftext],1);
  }
}'''
createView( db, "dateplaceprofanity", "new-view", mapFunction )