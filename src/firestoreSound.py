# https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/firestore/cloud-client/snippets.py
from firebase import Firebase
import firebase_admin
from firebase_admin import credentials, firestore
import uuid

class FirestoreSound(Firebase):

  firestore_db = None

  def __init__(self):
    Firebase.__init__(self)
    self.firestore_db = firestore.client()

  '''
    entry example:
    song = {
      'originalName': 'moroi.mp3',
      'displayName': 'moroi song'
    }
  '''
  def create(self, sound):
    uuidv4 = str(uuid.uuid4())
    self.firestore_db.collection('sounds').document(uuidv4).set({'originalName': sound['originalName'], 'displayName': sound['displayName'], 'playedTimes': 0})
    return uuidv4

  '''
    entry example:
    song = {
      'uuid': uuid,
      'originalName': 'moroi2.mp3',
      'displayName': 'moroi2 song'
    }
  '''
  def update(self, sound):
    self.firestore_db.collection('sounds').document(sound['uuid']).update({'originalName': sound['originalName'], 'displayName': sound['displayName']})
    return sound['uuid']
  
  '''
    entry example:
    song = {
      'uuid': uuid,
    }
  '''  
  def playedTimesIncrement(self, sound):
    self.firestore_db.collection('sounds').document(sound['uuid']).update({'playedTimes': firestore.Increment(1)})
    return sound['uuid']

  '''
    entry example:
    song = {
      'uuid': uuid,
    }
  '''
  def remove(self, sound):
    self.firestore_db.collection('sounds').document(sound['uuid']).delete()
  
  '''
    use example:
    sounds = firestore.findAll()
    for sound in sounds:
        print(sound.to_dict()) #print all infos related to one sound
        print(sound.to_dict()['playedTimes']) #print total of reproductions
  '''
  def findAll(self):
    return self.firestore_db.collection('sounds').get()