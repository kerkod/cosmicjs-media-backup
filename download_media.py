import urllib.request
import json

backup_file = 'bucket.json'

with open(backup_file) as json_file:
    data = json.load(json_file)
    for p in data['bucket']['media']:
        print('Downloading: ' + p['name'])
        url = p['location'] + '/' + p['name']
        urllib.request.urlretrieve(url, 'medias/' + p['name'])
