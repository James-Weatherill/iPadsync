import turtle as t
from time import sleep
# import pygame

i = 0
min = 0
sec = 0
# clock = pygame.time.Clock()

while i == 0:
    minStr = str(min)
    secStr = str(sec)
    t.write(minStr.zfill(2) + ':' + secStr.zfill(2), font=("Arial", 100, "normal"), align="center")
    sec += 1
    # clock.tick(1)
    sleep(1)
    t.reset()
    t.Screen().bgcolor('purple')
    t.hideturtle()
    if sec%60 == 0 and sec!=0:
        min += 1
        sec = 0
    
