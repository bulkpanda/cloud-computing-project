import logging
import couchdb
dbname='tweetsukraine'
dbaddress='http://admin:Royai99@127.0.0.1:5984/'
couch=couchdb.Server(dbaddress)
db=couch[dbname]

def createView( dbConn, designDoc, viewName, mapFunction ):
    data = {
            "_id": f"_design/{designDoc}",
            "views": {
                viewName: {
                    "map": mapFunction
                    }
            },
            "language": "javascript",
            "options": {"partitioned": False }
            }
    logging.info( f"creating view {designDoc}/{viewName}" )
    dbConn.save( data )

mapFunction = '''function (doc) {
                    if(doc.place.full_name){
                      emit(doc.place.full_name, 1);
                      }
                    }'''
createView( db, "DESIGN_DOC_NAME", "VIEW_NAME", mapFunction )