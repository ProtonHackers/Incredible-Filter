import twitter

t = twitter.Twitter(auth=twitter.OAuth(
    consumer_key='2OpqKP7HWETiLQfbkt8pvZJtt',
    consumer_secret='qBViiC6pOjKDoLuegYVcSUc5trlWsByuiH59a7YyLmgK3lo6X2',
    token='845769803084120064-ufOqpGZMPqWAmQWN6wglauxpRFYZaIb',
    token_secret='oqNzyouv3j9WLIdIG74bh3MXDNOk48igE83Ktlkqv8zAQ'
))
print (t.statuses.home_timeline())
