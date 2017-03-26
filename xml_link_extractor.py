opened = open('crediblerss.xml', 'r')
str = opened.read()
newstr = ''

while(str.find('<link>') != -1):
    newstr += str[str.find("<link>")+6: str.find("<link>",str.find("<link>")+1)]
    