#! /opt/homebrew/Cellar/python@3.10/3.10.9/libexec/bin/python

from colorama import Fore
from decimal import *

ANSWER = Decimal(3.0)
M1 = 2

for i in range (1,100000000):
    if i%2 == 1 and i != 0:
        PISUM = pow((-1), M1)*(4/Decimal((i-1+2)*(i+2)*(i+1+2)))
        ANSWER += PISUM
        M1 += 1

print(Fore.LIGHTYELLOW_EX + '\nHere is an approximation of pi:' + Fore.CYAN + '\n\n' + str(ANSWER) + '\n')
