import rssparser
import numpy
opened = open('incrediblerss.xml', 'r')
# opened = open('crediblerss.xml', 'r')

str = opened.read()
strarr = []

while(str.find('<link>') != -1):
    url = str[str.find("<link>")+6: str.find("</link>",str.find("<link>"))]
    if(url.find('rssmix') == -1):
        strarr.append (url )
    str = str[str.find("</link>")+1:]
print(strarr)
numpy.save('incrediblerss',strarr)

