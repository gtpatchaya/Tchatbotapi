from flask import Flask , jsonify
# --------------------------------------------

#------Additional from previous file-------
from random import randint
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

cred = credentials.Certificate("touchchatbot-wrwsxi-firebase-adminsdk-q5vsd-b11575accf.json")
firebase_admin.initialize_app(cred)
#------------------------------------------

import requests
from flask import request, jsonify

app = Flask(__name__)

@app.route('/getCollectionDetailByName')
def home():    
    query_parameters = request.args
    name_intent = query_parameters.get('name_intent')

    dbNameCollection = firestore.client()
    database_1 = dbNameCollection.collection(name_intent).stream()

    content = []
    data={}
        
    for doc in database_1:
        # data.description = doc.to_dict()
        intent = {}
        intent["IntentName"] = str(name_intent)
        intent["description"] =  doc.to_dict()
        description = intent["description"]
        description["textInput"] = doc.id
        content.append(intent)
    data["data"]= content

    return data

@app.route('/getAllCollectionDetail')
def getdataAllCollection() : 
    dbNameCollection = firestore.client()
    database_1 = dbNameCollection.collection('Default Fallback Intent').stream()
    database_2 = dbNameCollection.collection('Agree').stream()
    database_3 = dbNameCollection.collection('Dental').stream()
    database_4 = dbNameCollection.collection('Holiday').stream()
    database_5 = dbNameCollection.collection('HolidayMonth').stream()
    database_6 = dbNameCollection.collection('HolidayYear').stream()
    database_7 = dbNameCollection.collection('Maternity leave').stream()
    database_8 = dbNameCollection.collection('Ordination leave').stream()
    database_9 = dbNameCollection.collection('Personal leave').stream()
    database_10 = dbNameCollection.collection('Probation').stream()
    database_11 = dbNameCollection.collection('Salary Certificate').stream()
    database_12 = dbNameCollection.collection('Sick Leave').stream()
    database_13 = dbNameCollection.collection('Social Security').stream()
    database_14 = dbNameCollection.collection('TaxPayment').stream()
    database_15 = dbNameCollection.collection('Vacation Leave').stream()

    content = []
    data={}
    collectionData= []

    collectionData = [database_1,database_2,database_3,database_4,database_5,database_6,database_7,database_8,database_9,database_10,database_11,database_12,database_13,database_14,database_15]
    nameCollection = ['Default Fallback Intent','Agree','Dental','Holiday','HolidayMonth','HolidayYear','Maternity leave','Ordination leave','Personal leave','Probation','Salary Certificate','Sick Leave','Social Security','TaxPayment','Vacation Leave']
    for i in range(len(collectionData)):     
        for doc in collectionData[i]:
            intent = {}
            intent["IntentName"] = str(nameCollection[i])
            intent["description"] =  doc.to_dict()
            description = intent["description"]
            description["textInput"] = doc.id
            content.append(intent)
    
    data["data"]= content
    return data
    
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)