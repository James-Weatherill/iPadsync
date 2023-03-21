from random import uniform
from math import sqrt
from colorama import Fore
from time import sleep

def userNumInput():
    number = input(Fore.RESET + "Please type a number: ")
    if number.isnumeric():
        number = int(number)
        print(Fore.LIGHTRED_EX + "\nWe will now calculate pi using", number, "samples!")
        calcPi(number)
    else:
        print(Fore.RED + "\nInvalid input, please try an integer!")
        countdown1 = 3
        sleep(0.5)
        while countdown1>0:
            print(countdown1)
            countdown1 -= 1
            sleep(1)
        print("\n")
        userNumInput()

def calcPi(a):

    pointInCirc = 0
    totalPoint = 0
    i = 0

    while i <= a:
        x = uniform(0,1)
        y = uniform(0,1)
        if sqrt(x**2 + y**2) <= 1:
            pointInCirc += 1
        totalPoint += 1
        i += 1

    piVal = 4*(pointInCirc/totalPoint)
    printingPi(piVal)
    
def printingPi(b):
    print(Fore.LIGHTMAGENTA_EX + "\nYour calculated pi value is:" + Fore.GREEN, b, Fore.RESET)
    quitAndRestart()

def quitAndRestart():
    QR = input(Fore.RED + "\nIf you would like to Restart, type 'r', and if you would like to Quit, type 'q'!\n\nEnter here: " + Fore.CYAN)
    QR = QR.lower()
    if QR == 'r':
        print("\n")
        userNumInput()
    elif QR == 'q':
        print(Fore.GREEN + "\nThank you! Goodbye!" + Fore.RESET)
    else:
        print(Fore.YELLOW + "\nInvalid input! Try again:")
        countdown2 = 3
        sleep(0.5)
        while countdown2>0:
            print(countdown2)
            countdown2 -= 1
            sleep(1)
        quitAndRestart()
    
userNumInput()