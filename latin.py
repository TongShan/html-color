#coding:utf-8

print "Welcome to the English to Pig Latin translator!"

pyg = 'ay'
original = raw_input('please, input your word >' )
word = original.lower()

if len(original) > 0 and original.isalpha():
    first = word[0]
    if first in ["a","e", "i", "o", "u"]:
        new_word = word + pyg
        print new_word
    else:
        new_word = word[1:] + word[0] + pyg
        print new_word
else:
    print "empty"
