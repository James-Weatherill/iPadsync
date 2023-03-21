#! /opt/homebrew/Cellar/python@3.10/3.10.9/libexec/bin/python

import random
from colorama import Fore
from time import sleep

upStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowStr = 'abcdefghijklmnopqrstuvwxyz'
numStr = '0123456789'
symStr = '-_=+<>?#%&'

upList = ([*upStr])
lowList = ([*lowStr])
numList = ([*numStr])
symList = ([*symStr])

print('\nHello! Welcome to my Password Generator.\n\n'
      'This program will generate a secure password using a combination of:\n'
      ' 2 Upper-case letters\n'
      ' 2 Lower-case letters\n'
      ' 2 Numbers\n'
      ' 2 Symbols\n')

sleep(0.5)

print('We will use your First and Last name to make the password more secure.\n'
      'Start by typing your First name below:\n')

sleep(0.5)

fName = input('Your First name here: ' + Fore.CYAN)
lName = input(Fore.RESET + 'Your Last name here : ' + Fore.CYAN)

fNameUp = fName.title()[0]
fNameLow = fName.lower()[0]
lNameUp = lName.title()[0]
lNameLow = lName.lower()[0]

upList.remove(fNameUp)
lowList.remove(fNameLow)
upList.remove(lNameUp)
lowList.remove(lNameLow)

upRand = random.sample(upList, k=2)
lowRand = random.sample(lowList, k=2)
numRand = random.sample(numList, k=2)
symRand = random.sample(symList, k=2)

totalList = upRand + lowRand + numRand + symRand

random.shuffle(totalList)
finalPass = ''.join(totalList)

print(Fore.RESET + '\nThank you ' + fName + ' ' + lName + ', for taking part!\n')

sleep(0.5)

print('Your secure password is: ' + Fore.LIGHTMAGENTA_EX + finalPass + '\n')
