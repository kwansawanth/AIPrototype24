import requests
import json
     

url = 'http://127.0.0.1:5000/simpleAPI'
myobj = {'message_key': 'message_val',
         'msg':'พลอย ขวัญสวรรค์'}

x = requests.post(url, data = json.dumps(myobj))
     
