from firestoreConfig import FirestoreConfig
from os import walk

class Config:

  firebaseConfig = None

  def __init__(self):
    self.firebaseConfig = FirestoreConfig()


  def setupConfigFile(self):
    try:
        config = self.firebaseConfig.get()
        if config == None:
            raise Exception('Não existe registro de configuração.')

        sounds = self._validateFiles(config['audio_folder'])
        print('\nConfigurações encontradas e validadas!')
        return config['audio_folder'], sounds
    except:
        return self._createDefaultConfigFile()

  def _createDefaultConfigFile(self):
      try:
        print('\nConfiguração não encontrada.')  
        audioFolder = input('Inisira o path da pasta que estão os audios: ')
        sounds = self._validateFiles(audioFolder)
        self.firebaseConfig.create(audioFolder)
        print('Configurações salvas.')
        return audioFolder, sounds
      except Exception as e:
          print('Erro ao salvar configurações.')
          exit()

  def _validateFiles(self, path):
      songs = []
      try:
          _, _, filenames = next(walk(path))
          songs = [name for name in filenames if name.endswith('.mp3')]
      except:
          print('Path inválido: {}'.format(path))
          raise Exception('m={} path={} err=Path inválido'.format('validateFiles', path))

      if len(songs) == 0:
          print('Nenhum arquivo .mp3 foi encontrado em: {}'.format(path))
          raise Exception('m={} path={} err=Arquivos mp3 não encontrados'.format('validateFiles', path))
      
      return songs