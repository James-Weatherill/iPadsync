#! /opt/homebrew/Cellar/python@3.10/3.10.9/libexec/bin/python

from colorama import Fore
import numpy as np

ARRAY = np.zeros((100,100))
PRIMES = []

for num in range (1,1001):
    PRIMES.append(num)

a = 0
b = 0
c = 0
d = 0

for i in range (0,1000):
    ARRAY[a][b] = PRIMES[c]
    b += 1
    c += 1
    d += 1
    if (d%100 == 0):
        a += 1
    if b == 100:
        b -= 100

for row in range (0,100):
    for div2 in ARRAY[row]:
        if div2%2 == 0 and div2 != 2:
            ARRAY[(np.where(ARRAY == div2))] = 0

    for div3 in ARRAY[row]:
        if div3%3 == 0 and div3 != 3:
            ARRAY[(np.where(ARRAY == div3))] = 0

    for div5 in ARRAY[row]:
        if div5%5 == 0 and div5 != 5:
            ARRAY[(np.where(ARRAY == div5))] = 0

    for div7 in ARRAY[row]:
        if div7%7 == 0 and div7 != 7:
            ARRAY[(np.where(ARRAY == div7))] = 0

ARRAY[0][0] = 0
for j in range (0,10):
    if j == 0:
        print(Fore.RED + '\nThese are the primes between', j, 'and', ((j+1)*100))
        print(Fore.CYAN + str(ARRAY[j]))
    else:
        print(Fore.RED + '\nThese are the primes between', j*100+1, 'and', ((j+1)*100))
        print(Fore.CYAN + str(ARRAY[j]))        
