import csv
import hashlib
from HTMLParser import HTMLParser
import urllib2
import urllib
from urllib2 import urlopen
import traceback
import os
import re


def get_csv_rows(url):
    with open(url, 'rb') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                yield row[0]


class ImageScraper(HTMLParser):
    # num_recursions = 100
    links = set()

    def __init__(self, base_url):
        HTMLParser.__init__(self)
        self.base_url = base_url

    def error(self, message):
        print(message)

    def handle_starttag(self, tag, attrs):
        if tag == 'link':
            # print attrs
            # if ('type', 'application/rss+xml') in attrs:
            print attrs
            for (attr, value) in attrs:
                print(value)
                self.links.add(value)

    def image_links(self):
        return self.links

import xml.etree.ElementTree


def gather_image_links(base_url, url_type):
    html_string = ''
    try:
        req = urllib2.Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req)
        # if response.getheader('content-type') == 'text/html':
        html_bytes = response.read()
        html_string = html_bytes.decode('utf-8')
        e = xml.etree.ElementTree.parse('thefile.xml').getroot()
        finder = ImageScraper(base_url=base_url)
        finder.feed(data=html_string)
        return finder.image_links()
    except Exception:
        with open(url_type + '.txt', 'a') as f:
            f.write(base_url + "\n")
        # print('generic exception: ' + traceback.format_exc())
        return set()


def iterate_url_list(urls, type):
    for url in urls:
        yield gather_image_links(url, type)


def iterate_urls():
    # non_credible_urls = get_csv_rows(
    #     'opensources-master/notCredible/notCredible.csv')
    # credible_urls = get_csv_rows('opensources-master/credible/credible.csv')

    non_cred_rss = iterate_url_list(['http://www.rssmix.com/u/8230881/rss.xml'], "non-credible")
    print(list(non_cred_rss))
    credible_urls = iterate_url_list(['http://www.rssmix.com/u/8230879/rss.xml'], "credible")
    print(list(credible_urls))


iterate_urls()
