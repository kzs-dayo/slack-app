import requests

TOKEN = 'トークン'
CHANNEL = 'チャンネル名'

url = "https://slack.com/api/chat.postMessage"
headers = {"Authorization": "Bearer "+TOKEN}
data  = {
   'channel': CHANNEL,
   'text': 'hogehoge'
}
r = requests.post(url, headers=headers, data=data)
print("return ", r.json())