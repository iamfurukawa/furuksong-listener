from pygame import mixer
from time import sleep

from device import Device

class Player:

  selectedDevice = None
  lastUuid = None

  def __init__(self):
    device = Device()
    self.selectDevice = device.selectDevice()
    mixer.init(devicename=self.selectDevice)

  def playInVirtualCable(self, audio):
    mixer.music.load(open(audio, 'rb'))
    mixer.music.play()

  def stop(self):
    mixer.music.stop()
  
  def isPlaying(self):
    return mixer.music.get_busy()