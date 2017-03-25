#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
from newspaper import Article

URL = 'http://rss.cnn.com/rss/cnn_topstories.rss'


def encode(text):
    return text.encode('utf-8').strip()


d = feedparser.parse(URL)

for post in d.entries:
    title = encode(post.title)
    text = Article(encode(post.link))
    text.download()
    text.parse()
    text = encode(text.text)
    print('{} \n=============================================================\n{}\n'.format(title, text))
