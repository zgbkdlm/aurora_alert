import aurora_spider
import push_api

aSpider = Aurora_spider()
aPush = Push_api()

# Updating the forecast in cycle, Crontab is recommended.
forecast = aSpider.sniff_short()

# Check if need to send notification
kp_threshold = 6

# Call push api, so that the notification can be pushed to users.
aPush.tele_push(forecast)
