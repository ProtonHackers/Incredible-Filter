import twitter
import json
import ssl


def get_tweets (token='845769803084120064-ufOqpGZMPqWAmQWN6wglauxpRFYZaIb', secret='oqNzyouv3j9WLIdIG74bh3MXDNOk48igE83Ktlkqv8zAQ' ):
    # Temp fix, we should check the cert
    ssl._create_default_https_context = ssl._create_unverified_context
    t = twitter.Twitter(auth=twitter.OAuth(
        consumer_key='2OpqKP7HWETiLQfbkt8pvZJtt',
        consumer_secret='qBViiC6pOjKDoLuegYVcSUc5trlWsByuiH59a7YyLmgK3lo6X2',
        token=token,
        token_secret=secret
    ))

    return t.statuses.home_timeline(count=200)
def read_tweets():
    opened = open('data.txt', 'r')
    return json.loads(opened.read())

def final_called():
    jsong = get_tweets()
    with open('data.txt', 'w') as outfile:
        json.dump(jsong, outfile)
    # jsong = read_tweets()
    sites = open('file.txt', 'r')
    sitelist = json.loads(sites.read()).keys()
    print(sitelist)

    for a in jsong:

        if len(a['entities']['urls']) > 0:
            str = a['entities']['urls'][0]['expanded_url']

            str = ((str + '/')[str.find('//') + 2:str.find("/", str.find("//") + 2)])
            if "www." in str:
                str = str[4:]

            if str in sitelist:
                print (str)
                print(1)
                a['validity'] = 'False'
            else:
                a['validity'] = 'True'
        else: a['validity'] = 'n/a'
        for key, val in a.items():
            if key == "id_str":

                print("{} = {}".format(key, val))
    return (jsong)
