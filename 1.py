import string

before = list(string.ascii_lowercase)
after = chr(ord(c)+2) for c in before
after[before.index('y')] = 'a'
after[before.index('z')] = 'b'

trans = str.maketrans(''.join(before), ''.join(after))

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. """

text.translate(trans)
"map".translate(trans)
