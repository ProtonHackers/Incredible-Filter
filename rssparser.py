#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
from newspaper import Article

URL = 'http://rss.cnn.com/rss/cnn_topstories.rss'


def encode(text):
    return text.encode('utf-8').strip()


def generate_links_from_feed(url):
    feed = feedparser.parse(url)
    for post in feed.entries:
        yield encode(post.link)


def get_text_from_url(url):
    text = Article(encode(url))
    text.download()
    text.parse()
    return encode(text.text)


if __name__ == '__main__':
    for link in generate_links_from_feed(URL):
        print('{}\n\n\n'.format(get_text_from_url(link)))
