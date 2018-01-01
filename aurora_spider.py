import requests
import re
from bs4 import BeautifulSoup

class Aurora_spider:
    
    def __init__(self):
        self.url = 'http://www.aurora-service.eu/aurora-forecast/'
        self.a = 1
    
    def sniff_short(self):
        r = requests.get(self.url)
        html_content = r.text
        soup = BeautifulSoup(html_content)
        
        kp_value = soup.find_all(style="color: #0000ff;")
        p=r'\w\.\w\w$'

        return [re.findall(p, kp_value[0].text)[0],
            kp_value[1].text, re.findall(p, kp_value[2].text)[0],
            kp_value[3].text, re.findall(p, kp_value[4].text)[0],
            kp_value[5].text, re.findall(p, kp_value[6].text)[0]]

    def sniff_long(self):
        
