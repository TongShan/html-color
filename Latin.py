#!usr/bin/python
# coding:utf-8

pyg = 'ay'
original = raw_input('Enter a word:' )
word = original.lower()

def isalpha():
    first = word[0]
    if original.isalpha() and first in ["a", "i", "e", "o", "u"]:
        new_word = word + pyg
        print new_word
    else:
        new_word = word[1:] + word[0] + pyg
        print new_word

if len(original) > 0:
   print original 
else:
    print "empty"
        
    


