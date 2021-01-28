import requests
headers = {'X-Api-Key':'94f58baad0e740a5b90f0ea422a5a68c'}
url ='https://randommer.io/api/Card'
r=requests.get(url, headers=headers)
print(r.url)