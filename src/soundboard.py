from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import datetime

from ip import IPLocalizer
from player import Player
from config import Config
from sounds import Sounds
from realtimeFirestoreSound import RealtimeFirestoreSound

player = Player()
config = Config()
realtime = RealtimeFirestoreSound()
ipLocalizer = IPLocalizer()

path, soundsLocal = config.setupConfigFile()
audios = Sounds(soundsLocal)
audios.sync()

lastUuid = ''

def listener(event):
    data = event.data.split()[0]
    if data == 'awaiting-request-song':
        return

    
    if player.lastUuid == data and player.isPlaying():
      player.lastUuid = None
      player.stop()
      realtime.resetStatus()
      return
      
    player.stop()
    player.lastUuid = data
    realtime.resetStatus()
    
    for audio in audios.soundsFirestore:
      if audio.id == player.lastUuid:
        print('[{}] Audio requisitado: {} - {}'.format(datetime.datetime.now(), audio.to_dict()['originalName'], ipLocalizer.search(event.data)))
        player.playInVirtualCable(path + audio.to_dict()['originalName'])
        audios.firestoreSound.playedTimesIncrement({
          'uuid': player.lastUuid,
        })
    

realtime.createListenerAndRun(listener)
