#coding:utf8

import urllib,re

ocr = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
data = re.findall(r'<!--(.*?)-->', ocr, re.S)
data = data[1]
for i in set(data):
    print i, ':', data.count(i)

word = []
for i in data:
    if data.count(i) <= 1:
        word.append(i)
print ''.join(word)

