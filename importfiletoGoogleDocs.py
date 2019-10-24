import json
import requests

headers = {"Authorization": "Bearer #YOUR ACCESS TOKEN#"} # in 'YOUR ACCESS TOKEN' type your GDrive api OAuth token
para = {
    "name": "BattlePassNicknames.csv", # filename to be uploaded
    "parents": ["YOUR DGRIVE FOLDER ID"] # google docs folder id
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': ('application/csv',open("./BattlePassNicknames.csv", "rb"))
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
