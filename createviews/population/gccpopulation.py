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
import logging
import couchdb
dbname='populationdata'
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
  emit(doc.gccsa_code, doc.earners_persons);
}'''
createView( db, "gccpopulation", "new-view", mapFunction )
