message = b'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ' \
          b'ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. '
message2 = b'http://www.pythonchallenge.com/pc/def/map.html'

# "by hand" version
for i in range(0, len(message2)):
    letter = message2[i]
    if 97 <= letter <= 122:
        new_letter = letter + 2
        if new_letter > 122:
            new_letter -= 26

        print(chr(new_letter), end='')
    else:
        print(chr(letter), end='')
print()

# more efficient?........:
inString = "KOE"
outString = "MQG"
dict = str.maketrans(inString, outString)

