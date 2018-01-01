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
        
        return short_forecast
        
        
    def sniff_long(self):
        a=1
