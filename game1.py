import string

def word(str):
    ans = ''
    for c in str :
            if c.isalpha():
		    tmp = ord(c)+2
		    if tmp > ord('z'):
			    tmp -= 26
		    ans += chr(tmp)
	    else:
		    ans += c
    print ans


str1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

str2 = 'map'

word(str1)
word(str2)


