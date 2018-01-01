import aurora_spider

aSpider = Aurora_spider()

# Updating the forecast in cycle
forecast = aSpider.sniff_short()

# Call alert api, for example SMS, email, Telegram Bot etc.
