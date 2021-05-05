import firebase_admin
from firebase_admin import credentials, firestore

class Firebase:

  def __init__(self):    
    if not firebase_admin._apps:
      cred = credentials.Certificate('src/credentials.json')
      database = {'databaseURL': 'https://furuksong-default-rtdb.firebaseio.com/'}
      firebase_admin.initialize_app(cred, database)