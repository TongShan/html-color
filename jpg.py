#!/ust/bin/python

import re
import urllib2

def Html(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

def Img(html):
    photo = r'src="(.*?\.jpg)" width'
    image = re.compile(photo)
    imagelist = re.findall(image,html)
    x = 0
    for j in imagelist:
        urllib2.urlretrieve(j, '%s.jpg' % x)
        x += 1

html = Html("http://tieba.baidu.com/p/2256306796")
Img(html)
