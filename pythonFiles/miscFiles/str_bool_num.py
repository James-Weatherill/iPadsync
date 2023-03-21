#! /opt/homebrew/Cellar/python@3.10/3.10.9/libexec/bin/python

from colorama import Fore

i = 0
print(Fore.GREEN + "Welcome to my type classifier!" + Fore.RESET)
while i<1:
    global what
    what = input("""\nPlease input some characters
or Enter 'EXIT' to end the program: """)
    if what == 'EXIT':
        print("\nGoodbye!")
        i += 1
    elif what.isnumeric() and int(what) != 1 and int(what) != 0:
        print("\n" + what, "is a Number")
    elif what == "1" or what == "0":
        print("\nDid you mean the Boolean or the Integer?")
        def boolOrInt():
            boolInt = input("\nType 'b' for Boolean, and 'i' for Integer: ")
            boolInt = boolInt.lower()
            if boolInt == "b":
                if what == "1":
                    print("\nTrue is a Boolean")
                elif what == "0":
                    print("\nFalse is a Boolean")
            elif boolInt == "i":
                print("\n" + what, "is a Number")
            else:
                print("\ninvalid, try again")
                boolOrInt()
        boolOrInt()
    elif what == "True" or what == "False":
        print("\nDid you mean the Boolean or the String?")
        def boolOrStr():
            boolStr = input("\nType 'b' for Boolean, and 's' for String: ")
            boolStr = boolStr.lower()
            if boolStr == "b":
                if what == "True":
                    print("\nTrue is a Boolean")
                elif what == "False":
                    print("\nFalse is a Boolean")
            elif boolStr == "s":
                print("\n" + what, "is a String")
            else:
                print("\ninvalid, try again")
                boolOrStr()
        boolOrStr()
    else:
        print("\n" + what, "is a String")