from firebase import Firebase
import firebase_admin
from firebase_admin import credentials, firestore

class FirestoreConfig(Firebase):

  firestore_db = None

  def __init__(self):
    Firebase.__init__(self)
    self.firestore_db = firestore.client()

  def create(self, audioFolder):
    self.firestore_db.collection('configurations').document('iamfurukawa').set({'audio_folder': audioFolder})

  def update(self, audioFolder):
    self.firestore_db.collection('configurations').document('iamfurukawa').update({'audio_folder': audioFolder})
    
  def get(self):
    return self.firestore_db.collection('configurations').document('iamfurukawa').get().to_dict()