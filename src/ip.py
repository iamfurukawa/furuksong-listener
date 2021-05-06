import requests
import json

class IPLocalizer:

  ipTables = {}

  def __init__(self):
    self.ipTables = {}


  def search(self, data):
    ip = ''
    try:
      ip = data.split()[1]
    except Exception as e:
      return data

    if ip in self.ipTables:
      return self.ipTables[ip]

    url = 'https://ipinfo.io/{}/json'.format(ip)
    res = requests.get(url=url)
    data = res.json()
    info = '{} - {}/{}'.format(ip, data['city'], data['region'])
    self.ipTables.update({ip: info})
    return self.ipTables[ip]