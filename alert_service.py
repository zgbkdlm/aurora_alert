import aurora_spider
import push_api

aSpider = aurora_spider.Aurora_spider()
aPush = push_api.Push_api()

# Updating the forecast in cycle, Crontab is recommended.
forecast = aSpider.sniff_short()

# Check if need to send notification
kp_threshold = 1
w = [z[0] for z in enumerate(list(map(float,[forecast[2], forecast[4], forecast[6]]))) if z[1] > kp_threshold]
if w != []:
    w = w[0]
    push_text = "Aurora alert! The Kp value is predicted to reach " + forecast[2*w+2] + " in " + forecast[2*w+1] + " minutes. " \
                                                                                               "The current Kp is " + forecast[0]
    # Call push api, so that the notification can be pushed to users.
    aPush.tele_push(push_text)
    # aPush.***** Put your services here