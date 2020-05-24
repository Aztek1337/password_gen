# AA Test, Password generator

import sys
import random
import string
import secrets

intro =\
"""
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                     AA Password Generator	                                        |
 |                                      - Version: 1.0 -                                                |
 |                                   - By aa@aztek.xyz -                                               |
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

int_arg = 0
try:
    int_arg = int(sys.argv[1], base=10)

except:
    print("ERROR! Please only enter a base 10 number!")

def randomstring(stringlength):
    securestr = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for char in range(stringlength)))
    return securestr

user_choice = int(int_arg)
print(randomstring(user_choice))
