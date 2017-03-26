#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import json
import ssl
from website.predict_cyber import bully_analysis


def get_tweets(token='845769803084120064-ufOqpGZMPqWAmQWN6wglauxpRFYZaIb',
               secret='oqNzyouv3j9WLIdIG74bh3MXDNOk48igE83Ktlkqv8zAQ'):
    # Temp fix, we should check the cert
    ssl._create_default_https_context = ssl._create_unverified_context
    t = twitter.Twitter(auth=twitter.OAuth(
        consumer_key='2OpqKP7HWETiLQfbkt8pvZJtt',
        consumer_secret='qBViiC6pOjKDoLuegYVcSUc5trlWsByuiH59a7YyLmgK3lo6X2',
        token=token,
        token_secret=secret
    ))

    return t.statuses.home_timeline(count=20)


def read_tweets():
    opened = open('data.txt', 'r')
    return json.loads(opened.read())


def final_called(jsong):
    with open('data.txt', 'w') as outfile:
        json.dump(jsong, outfile)

    sites = open('website/file.txt', 'r')
    sitelist = json.loads(sites.read()).keys()
    print(sitelist)
    val = 0
    arr = []
    for a in jsong:
        print(a)
        text = a['text']
        if val == 30:
            break
        if len(a['entities']['urls']) > 0:
            str = a['entities']['urls'][0]['expanded_url']

            str = ((str + '/')[str.find('//') + 2:str.find("/", str.find("//") + 2)])
            if "www." in str:
                str = str[4:]

            if str in sitelist:
                print(str)
                print(1)
                a['validity'] = 'False'
            else:
                a['validity'] = 'True'
        else:
            a['validity'] = 'n/a'
        if bully_analysis(text) == 0:
            a['harass'] = "True"
        else:
            a['harass'] = "False"
        arr.append(a)
        val += 1

    return arr


final_called(get_tweets())
