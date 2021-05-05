from firestoreSound import FirestoreSound
import json

class Sounds:
  
  # Firestore connection
  firestoreSound = None

  # Data from firestore
  soundsFirestore = []

  # Sets
  soundsLocalSet = set()
  soundsFirestoreSet = set()

  def __init__(self, soundsLocal):
    self.firestoreSound = FirestoreSound()
    self.soundsLocalSet = set(soundsLocal)
    self.soundsFirestore = self.firestoreSound.findAll()
    self.soundsFirestoreSet = set([(sound.to_dict()['originalName']) for sound in self.soundsFirestore])

  
  def sync(self):
    self._remove(self.soundsFirestoreSet.difference(self.soundsLocalSet))
    self._create(self.soundsLocalSet.difference(self.soundsFirestoreSet))
    self._update()

    self.soundsFirestore = self.firestoreSound.findAll()
    self.soundsFirestoreSet = set([(sound.to_dict()['originalName']) for sound in self.soundsFirestore])

  def _remove(self, soundsToRemove):
    if len(soundsToRemove) == 0:
      print('Nenhum audio pra ser removido.')
      return 

    for soundName in soundsToRemove:
      for sound in self.soundsFirestore:
        if sound.to_dict()['originalName'] == soundName:
          self.firestoreSound.remove({
            'uuid': sound.id,
          })

    print('Audios removidos: {}'.format(soundsToRemove))

  def _create(self, soundsToCreate):
    if len(soundsToCreate) == 0:
      print('Nenhum audio pra ser criado.')
      return 

    for soundName in soundsToCreate:
      self.firestoreSound.create({
        'originalName': soundName,
        'displayName': soundName.replace('.mp3', '').replace('-', ' ').replace('_', ' ').strip()
      })

    print('Audios criados: {}'.format(soundsToCreate))

  def _update(self):
    try:
      with open('src/update.json') as json_file:
        data = json.load(json_file)

        if len(data['sounds']) == 0:
          print('Nenhum audio pra ser atualizado.')
          return

        uuid = []
        for p in data['sounds']:
          uuid.append(p['uuid'])
          self.firestoreSound.update({
            'uuid': p['uuid'],
            'originalName': p['originalName'],
            'displayName': p['displayName'],
          })

        print('Audios atualizados: {}'.format(uuid))
    except Exception as e:
      print('Erro ao ler o arquivo update.json')