#6-2

import string
import keyword

alphas = string.letters + '_'
nums = string.digits
alphanumeric = alphas + nums
keywordhad = keyword.kwlist

print 'Welcome to the Identifier Check v1.0'
myInput = raw_input('Identifier to test?')

if len(myInput) > 0:

    if myInput[0] not in alphas:
         print '''invalid:first symbol must be alphabetic'''
    else:
        if myInput in keywordhad:
            print '''invalid:can not be keyword'''
        else:
            for otherChar in myInput[1:]:

                if otherChar not in alphanumeric:
                    print '''invalid: remaining symbols must be alphanumeric'''
                    break

            else:
                print "okay as an identifier"
