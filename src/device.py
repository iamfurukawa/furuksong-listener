from pygame._sdl2 import get_num_audio_devices, get_audio_device_name
from pygame import mixer

class Device:

  deviceName = None

  def __init__(self):
    pass

  def selectDevice(self):
    mixer.init()
    playbacks = [get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))]
    mixer.quit()

    device = None
    for playback in playbacks:
        if 'VoiceMeeter' in playback:
            device = playback

    if device is None:
        print('\nVocê não possui nenhum dispositivo virtual de audio.')
        exit()

    print('\nDispositivo de saída selecionado: {}.'.format(device))
    return device