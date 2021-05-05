from firebase import Firebase
import firebase_admin
from firebase_admin import credentials, db, firestore
from time import sleep

class RealtimeFirestoreSound(Firebase):

  realtime_db = None

  def __init__(self):
    Firebase.__init__(self)
    

  def resetStatus(self):
    db.reference('RequestSoundMonitoring').set('awaiting-request-song')

  def createListenerAndRun(self, listener):
    conn = db.reference('RequestSoundMonitoring').listen(listener)
    
    try:
        while True:
          sleep(1)
    except KeyboardInterrupt:
        conn.close()