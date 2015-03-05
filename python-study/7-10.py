#7-10

import string

alphas = string.letters

def rot(startw):

    endw = ''
    for i in startw:
        if i in alphas:
            if ('A' <= i <= 'M') or ('a' <= i <= 'm'):
                endw += chr(ord(i)+13)
            else:
                endw += chr(ord(i)-13)
                #chr(ord(i)+13-26)
        else:
            endw += i
    return endw

print '%rot13.py'

myInput = raw_input('Enter string to rot13: ')

print 'Your string to en/decrypt was: ',[rot(myInput)]
