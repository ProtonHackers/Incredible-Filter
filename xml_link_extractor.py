import rssparser
import numpy
#opened = open('incrediblerss.xml', 'r')
opened = open('crediblerss.xml', 'r')

str = opened.read()
strarr = []
i =0
while(str.find('<link>') != -1 and i<164):
    i +=1
    url = str[str.find("<link>")+6: str.find("</link>",str.find("<link>"))]
    if(url.find('rssmix') == -1):
        print(url)
        try:
            strarr.append (rssparser.get_text_from_url(url) )
        except:
            pass
        print(strarr)
    str = str[str.find("</link>")+1:]
print(strarr)
numpy.save('crediblerss',strarr)

