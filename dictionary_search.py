import requests,json

word = input('Word? ')
url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/'+word
response = requests.get(url).text
resp = json.loads(response)
print(word +'.'+ resp[0]['meanings'][1]['partOfSpeech'] +'.'+ resp[0]['meanings'][1]['definitions'][0]['definition'])