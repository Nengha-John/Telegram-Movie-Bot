import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

def storeToCloud(data):
     path = "DumbsterBot/dumbsterFirestore.json"
     cred = credentials.Certificate(path)
     firebase_admin.initialize_app(cred)
     db = firestore.client()
     ref = db.collection('requests')
     file  = json.dumps(data)
     loadedFile = json.loads(file)
     ref.add(loadedFile)