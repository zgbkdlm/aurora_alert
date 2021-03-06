import push_config
import requests
import json

class Push_api():
    
    def __init__(self):
        self.url = "https://api.telegram.org/bot" + push_config.bot_token + "/"
        self.chat_id = "0"

    # Push for Telegram Bot
    def tele_push(self, content):
        if self.tele_get_id():
            r = requests.post(self.url + "sendMessage", 
                              data={'chat_id':self.chat_id, 'text':content})

    def tele_get_id(self):
        r = requests.get(self.url + "getUpdates")
        r = json.loads(r.text)
        if r["ok"] == True:
            self.chat_id = r["result"][0]["message"]["chat"]["id"]
            return True

    # Here define other push services like SMS, email, whatsapp etc.