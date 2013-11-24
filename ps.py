#coding:utf8

class Ren():
    name = "人类"

    def say(self):
        print "会说话"

class Chinese(Ren):
    name = "中国人"

    def say(self):
        print "会说中国话"

milo = Ren()
print milo.name
milo.say()
li = Chinese()
print li.name
li.say()
