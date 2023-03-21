#! /opt/homebrew/Cellar/python@3.10/3.10.9/libexec/bin/python

## ~ James Weatherill ~
## ~ 21/01/2023 ~
## ~ First attempt at trying to use PyGame ~

import pygame   # PyGame, for all of the functions.
import random   # random, to randomise the locations of food for the snake to eat!
from time import sleep  # sleep, to pause the code temporarily.
from pathlib import Path    # pathlib, for easy file path managment.
pygame.font.init()  # Font module for PyGame.


def configs(WIDTHNUM, HEIGHTNUM, FPSNUM):  # My 'config' function.

    global OFFSET
    OFFSET = 40 # Declaring the amount of space that the top bar takes up.

    global WIDTH, HEIGHT, WIN
    WIDTH, HEIGHT = WIDTHNUM, HEIGHTNUM   # Width and Height of game display.
    WIN = pygame.display.set_mode((WIDTH, HEIGHT+OFFSET))  # Assigning display to variable.
    pygame.display.set_caption('Snake!')  # Making a display title.

    global FPS
    FPS = FPSNUM  # Setting the display at 8 FPS.

    global SNAKELIST
    SNAKELIST = []   # The empty list where all snakle positions will be stored

    global BROWNCHECK
    BROWNCHECK = pygame.transform.scale(pygame.image.load(
        Path('Assets', 'brown_check.png')), (WIDTH, HEIGHT))    # The brown checkerboard pattern file.
    
    global FILE
    FILE = Path('Assets', 'highscore.txt')  # Setting FILE to the highscore.txt file.

    global ROSE, LIME, WHITE, BLUE, GREY, RED
    ROSE = (221, 60, 106)   # Used for food.
    LIME = (218, 247, 166)  # Used for the snake.
    WHITE = (255, 255, 255) # Used for text.
    BLUE = (70, 130, 180) # Used for title and restart text.
    GREY = (100, 100, 100) # Used for end text.
    RED = (255, 0, 0) # Used for quit text.

    global SCOREFONT
    SCOREFONT = pygame.font.SysFont('Helvetica', 20, True, False)   # Setting fonts for future blits.

    global TIMERFONT
    TIMERFONT = pygame.font.SysFont('Helvetica', 20, False, False)

    global HISCOREFONT
    HISCOREFONT = pygame.font.SysFont('Calibre', 30, False, False)

    global DEATHFONT
    DEATHFONT = pygame.font.SysFont('Calibre', 60, False, False)
    
    global EXIT1FONT
    EXIT1FONT = pygame.font.SysFont('Calibre', 25, False, False)

    global EXIT2FONT
    EXIT2FONT = pygame.font.SysFont('Calibre', 25, False, False)

    global THANKYOUFONT1, THANKYOUFONT2
    THANKYOUFONT1 = pygame.font.SysFont('Calibre', 60, True, False)
    THANKYOUFONT2 = pygame.font.SysFont('Calibre', 60, False, False)

def snakeandfood(SPEED, XSTART, YSTART, XMOVE, YMOVE):     # Main body function.

    clock = pygame.time.Clock()     # setting 'clock' to the define number of loops per second.

    SCORECOUNT = 0  # Creating variables
    TIMERCOUNT = 0

    SNAKELENGTH = 1

    AB = 0
    CD = 0

    SANDFWIDTH = 25
    SANDFHEIGHT = 25

    FOODX = 475
    FOODY = 250+OFFSET   # This variable can move along with a change in OFFSET

    EXITREQ = True

    SCORETEXT = SCOREFONT.render('Score: ', 1, WHITE)

    run = True
    while run:
        clock.tick(FPS)     # Clock starts ticking at 8 FPS.
        PREVX, PREVY = XMOVE, YMOVE # Keeps a variable before current Pos gets changed.
        for event in pygame.event.get():    # Gets the current 'event' state of the display.
            if event.type == pygame.QUIT:   # Checks if the user has tried to close.
                run = False
            elif event.type == pygame.KEYDOWN:  # Begins looking for keys being pressed.
                if event.key == pygame.K_a and PREVX != SPEED:
                    XMOVE = -SPEED      # XMOVE becomes '-25'.
                    YMOVE = 0
                elif event.key == pygame.K_d and PREVX != -SPEED:
                    XMOVE = SPEED       # XMOVE becomes '25'.
                    YMOVE = 0
                elif event.key == pygame.K_w and PREVY != SPEED:
                    XMOVE = 0
                    YMOVE = -SPEED
                elif event.key == pygame.K_s and PREVY != -SPEED:
                    XMOVE = 0
                    YMOVE = SPEED
        XSTART += XMOVE     # If XMOVE has been changed, x position will change.
        YSTART += YMOVE

        WIN.fill(BLUE)  # Fills screen with Blue.
        WIN.blit(BROWNCHECK, (0, OFFSET))    # Sets checkerboard over the Blue backround.

        SNAKEHEAD = []  # Creating empty list to contain current snake head position.
        SNAKEHEAD.append(XSTART)    # Appends list for x and y pos.
        SNAKEHEAD.append(YSTART)
        SNAKELIST.append(SNAKEHEAD) # Appends full snake Pos list.
        if len(SNAKELIST) > SNAKELENGTH:    # Checks if theres more positions in the list than number of snake segments.
            del SNAKELIST[0]    # Will delete the ftail segment if True ^^.
        for p in SNAKELIST:
            pygame.draw.rect(WIN, LIME, [p[0], p[1], SANDFWIDTH, SANDFHEIGHT]) # Draws rect for each position in SNAKELIST.

        for collision in SNAKELIST[:-1]:
            if collision == SNAKEHEAD:  # Checks if current head Pos == any Pos in SNAKELIST (hits itself).
                run = False 

        if FOODX == XSTART and FOODY == YSTART:
            FOODX = (random.randint(0, 23))*25  # Randomly selected x and y position.
            FOODY = (random.randint(0, 23))*25+OFFSET
            SCORECOUNT += 1 # Adds 1 to the score.
            SNAKELENGTH += 1    # Increases the total number of segments.
            SCORETEXT = SCOREFONT.render('Score: ' + str(SCORECOUNT), 1, WHITE)

        CURRENTHI = FILE.read_text()    # Reads a highscore plain text files.
        if int(CURRENTHI) < SCORECOUNT: # Checks if users current score is higher than high score.
            FILE.write_text((FILE.read_text()).replace(CURRENTHI, str(SCORECOUNT))) # Will ammend file.
        HISCORETEXT = HISCOREFONT.render('Hi Score:  ' + FILE.read_text(), 1, WHITE)    # Puts highscore on screen.

        TIMERCOUNT += (1/8) # Adds an 8th of a second per frame.
        if round(TIMERCOUNT) == 60: # When time equal a minute, set to 0.
            CD += 1
            TIMERCOUNT = 0
        TIMERTEXT = TIMERFONT.render('hr: (' + str(AB) + ') m: (' + str(CD) + ') s: (' + str(round(TIMERCOUNT)) + ')', 1, WHITE)

        if XSTART < 0 or YSTART < 25 or XSTART > (WIDTH-25) or YSTART > (HEIGHT+25):  # Sets screen boundaries where snake dies.
            run = False

        pygame.draw.rect(WIN, ROSE, [FOODX, FOODY, SANDFWIDTH, SANDFHEIGHT])  # Shows food.
        WIN.blit(SCORETEXT, (5, 11.5))  # Shows text at the top of the screen.
        WIN.blit(TIMERTEXT, (210, 11.5))
        WIN.blit(HISCORETEXT, (460, 11.5))
        if run == False:
            WIN.fill(BLUE)  # Resets screen, to full cover dead snake.
            WIN.blit(SCORETEXT, (5, 11.5))
            WIN.blit(TIMERTEXT, (210, 11.5))
            WIN.blit(HISCORETEXT, (460, 11.5))
            WIN.blit(BROWNCHECK, (0, OFFSET))
            pygame.draw.rect(WIN, ROSE, [FOODX, FOODY, SANDFWIDTH, SANDFHEIGHT])
            DEATHTEXT = DEATHFONT.render('GAME OVER  Score: ' + str(SCORECOUNT), 1, WHITE)
            EXIT1TEXT = EXIT1FONT.render('press return/enter to exit', 1, RED)
            EXIT2TEXT = EXIT2FONT.render("or press 'r' to restart!", 1, BLUE)
            THANKYOUTEXT1 = THANKYOUFONT1.render('Thank you', 1, GREY)
            THANKYOUTEXT2 = THANKYOUFONT2.render('for playing!', 1, GREY)
            WIN.blit(DEATHTEXT, (75, 260))  # Blits the finishing text.
            WIN.blit(EXIT1TEXT, (200, 310))
            WIN.blit(EXIT2TEXT, (220, 330))
            pygame.display.update()  # Updates the screen using new above changes.
            while EXITREQ:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:    # Will exit out of the game.
                            EXITREQ = False
                            WIN.blit(BROWNCHECK, (0, OFFSET))
                            pygame.draw.rect(WIN, ROSE, [FOODX, FOODY, SANDFWIDTH, SANDFHEIGHT])
                            WIN.blit(THANKYOUTEXT1, (170, 260))  # Thank you for playing.
                            WIN.blit(THANKYOUTEXT2, (185, 300))
                            pygame.display.update()  # Updates screen for end of game.
                            sleep(1.5)  # Pauses code for 1.5 seconds.
                        if event.key == pygame.K_r:  # Restarts game from beginning.
                            EXITREQ = False
                            run = True
                            del SNAKELIST[:-1]  # Resets snake length back to 1 so that it fits on the screen.
                            snakeandfood(25, 100, 250+OFFSET, 0, 0)  # Launches snakeandfood() from start

        pygame.display.update()     # Full display gets update

    pygame.quit()   # Kills the PyGame window 

if __name__ == "__main__":  # If the file is the original file the code was written, then...
    configs(600, 600, 8)   # WIDTHNUM, HEIGHTNUM, FPSNUM
    snakeandfood(25, 100, 250+OFFSET, 0, 0)  # SPEED, XSTART, YSTART, XMOVE, YMOVE
