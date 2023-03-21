#! /opt/homebrew/Cellar/python@3.10/3.10.9/libexec/bin/python

# The purpose of this code is to find the ideal room prices for the house in Year 3.
# It will calculate the square meters of each bedroom, and find its % of total bedroom area.
# The % of total room area will be multiplied by price (minus utilities).
# We then add the utility price per room back to the figures. This gives us a rough number.
# We then adjust these numbers by eye and make final, more round, prices (in £).

# Here we are importing a library that pauses the code for 'x' amount of time.
from time import sleep
from colorama import Fore

# These four lines set the square meters for each room.
b1 = 11.83
b2 = 12.08
b3 = 11.47
b4 = 5.59
# This line calculates the total area of the rooms.
totalRArea = (b1+b2+b3+b4)

# This is the total house of the price, with no adjustments.
totalHPrice = 2300
# Here we calculate the total value of the rooms (assuming that 1/3 of the house is public).
totalRPrice = round(2300*(2/3))
# This line shows us the price of utilities in the house (approx 1/3 of total price).
utilPrice = totalHPrice-totalRPrice
# This calculates the price per person that is paid for utilities
roomUtilPrice = round(utilPrice/4)

# These lines calculate the square meter share that each room has of the total.
b1Perc = b1/totalRArea
b2Perc = b2/totalRArea
b3Perc = b3/totalRArea
b4Perc = b4/totalRArea

# We use the percentages to find price per m^2.
b1Price = round(b1Perc*totalRPrice)
b2Price = round(b2Perc*totalRPrice)
b3Price = round(b3Perc*totalRPrice)
b4Price = round((b4Perc*totalRPrice)-1)

# These ar manually corrected prices for the rooms, by eye.
finalB1Price = ((b1Price-25)+roomUtilPrice)
finalB2Price = ((b2Price-34)+roomUtilPrice)
finalB3Price = ((b3Price-41)+roomUtilPrice)
finalB4Price = ((b4Price+100)+roomUtilPrice)

# James and Siana have a separate agreement for prices.
b3Agree = (finalB3Price-10)
b4Agree = (finalB4Price+10)

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Below here is printing all the important variables, and showing each important step.
print('\nTotal Price of Rooms:', Fore.GREEN+ '£' + str(totalRPrice))

sleep(0.5)

print(Fore.RESET + '\nRelative Price of Room 1:', Fore.GREEN + '£' + str(b1Price))
print(Fore.RESET + 'Relative Price of Room 2:', Fore.GREEN + '£' + str(b2Price))
print(Fore.RESET + 'Relative Price of Room 3:', Fore.GREEN + '£' + str(b3Price))
print(Fore.RESET + 'Relative Price of Room 4:', Fore.GREEN + '£' + str(b4Price))

sleep(0.5)

print(Fore.RESET + '\nRoom 1 Price including Utilities:', Fore.GREEN + '£' + str(b1Price+roomUtilPrice))
print(Fore.RESET + 'Room 2 Price including Utilities:', Fore.GREEN + '£' + str(b2Price+roomUtilPrice))
print(Fore.RESET + 'Room 3 Price including Utilities:', Fore.GREEN + '£' + str(b3Price+roomUtilPrice))
print(Fore.RESET + 'Room 4 Price including Utilities:', Fore.GREEN + '£' + str(b4Price+roomUtilPrice))

sleep(0.5)

print(Fore.RESET + "\nZoie's  room, Final Price:", Fore.CYAN + "£" + str(finalB1Price))
print(Fore.RESET + "Ella's  room, Final Price:", Fore.CYAN + "£" + str(finalB2Price))
print(Fore.RESET + "Siana's room, Final Price:", Fore.GREEN + "£" + str(finalB3Price))
print(Fore.RESET + "James'  room, Final Price:", Fore.GREEN + "£" + str(finalB4Price))

sleep(0.5)

print(Fore.RESET + "\nSiana's room, adjusted Final:", Fore.CYAN + "£" + str(b3Agree))
print(Fore.RESET + "James'  room, adjusted Final:", Fore.CYAN + "£" + str(b4Agree) + Fore.RESET + '\n')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
