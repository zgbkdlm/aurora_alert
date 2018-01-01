import push_config
import requests

class Push_api():
    
    def __init__(self):
        
    def tele_push(self, content):
        url = "https://api.telegram.org/bot" + bot_token + "/"
        r = request.get(url + getUpdates)
        r = requests.post(url + "sendMessage", 
                          data={'chat_id':chat_id, 'text':'ttttttt'})
