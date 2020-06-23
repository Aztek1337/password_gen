# AA Test, Password generator

import random,string,secrets

intro =\
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                     AA Password Generator	                                       |
|                                      - Version: 2.0 -                                                |
|                                   - By aa@aztek.xyz -                                                |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
print(intro + "\n\n")

print("Levels of Complexity:\n")
print("[1] High Complexity - letters,digits & special characters\n[2] Medium Complexity - letters & digits\n[3] Low Complextity - only letters\n")
int_arg = input("Please enter the number assoicated with the complexity level you wish the password to be generated with: \n")
int_arg = int(int_arg)

if int_arg > 3:
    print("ERROR! Please only select numbers 1 2 or 3")
else:
    char_num = input("\nPlease enter the number of characters you would like this password to be: \n")
    char_num = int(char_num)

def randomstring1(stringlength):
    securestr = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for char in range(stringlength)))
    return securestr

def randomstring2(stringlength):
    securestr = ''.join((secrets.choice(string.ascii_letters + string.digits) for char in range(stringlength)))
    return securestr

def randomstring3(stringlength):
    securestr = ''.join((secrets.choice(string.ascii_letters) for char in range(stringlength)))
    return securestr

if int_arg == 1:
    print(randomstring1(char_num))
elif int_arg ==2:
    print(randomstring2(char_num))
elif int_arg ==3:
    print(randomstring3(char_num))
else:
    print("\n")
