import urllib
import string
import re

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
html = urllib.urlopen(url).read()

f = re.findall(r'%%.*?-->', html,re.S)
contents = f.read()

chlist = []
for ch in f:
    if ch in string.lowercase\
            and ch not in string.whitespace:
        chlist.append(ch)

print "".join(chlist)

