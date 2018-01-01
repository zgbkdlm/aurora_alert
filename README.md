# Aurora Alert API
Multiple alert api for you not to miss beautiful aurora. 

# Dependency:
BeautifulSoup 4  
http://www.aurora-service.eu/

# Installation:
```
git clone https://github.com/zgbkdlm/aurora_alert.git
pip3 install beautifulsoup4
```
# How to use?
The alert application consists of three independent parts: aurora spider, push service and cycle.

What you have to do is to write your own push program in ```push_api.py```  

Note that a Telegram Bot push service has been written for you in advance. You have to create your own bot and start a chat with it first.

After all that, write a suitable crontab for ```alert_service.py```, for example:  
```
*/30 * * * * python3 /path-to/alert_service.py
```
 
Or, you can also treat alert_service as daemon process. 