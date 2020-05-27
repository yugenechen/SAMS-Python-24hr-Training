# -*- coding: utf-8 -*-
"""
Python_Sams21, p 241-260, Making Games with Pygame \
Best Reference:  https://www.pygame.org/docs/index.html
others:  pyglet for 3-D games:  http://pyglet.org
Packaging your game for distribution:  http://pyinstaller.org
[zork, Adventure are good examples of early text-based games]
1. What does pygame provide?
    [answer]:  open source library for building desktop applications. Always
               spelled in all lowercase- "pygame".
               pygame (the library) is a Free and Open Source python programming\
               language library for making multimedia applications like games.
               pygame.org (the website) welcomes all Python game, art, music, \
               sound, video and multimedia projects.

2. Installing pygame
    [answer]:  A Windows and MAC installer exists -
    http://www.pygame.org/download.shtml
     uninstall old versions of pygame first before installing a newer version.
     Note:  Conda does not suppot pygame.
             must use pip.
             1. open a python cmd.exe (or open Anaconda Navigator cmd.exe)
             2. py -m pip install -U pygame --user
             3. test it using a built-in exampel:
                py -m pygame.examples.aliens

3. Create screens in Pygame
[answer]:  screen = pygame.display.set_mode((x,y))
          where (x,y) is the (width, tall) in pixels.
          see:  ch21_lesson31 and ch21_lesson32 (code lessons below)

4. Create shapes in Pygame
[answer]:    pygame.draw.<shape>(scree, <colorName>,<coordinates>)
ex. circle:  pygame.draw.circle(screen, RED, (20,20), 10)
             where (20,20) = center coordinates, 10 = radius length
             where (x,Y) = (fromLeft, fromTop)

5. How to move shapes
[answer]:  Increment the shape coordinates each execution or based on keyboard
           or mouse input.

6. How to get User Input
[answer]:  from pygame.locals import *
         # captures every key and button click on the keyboard and mouse.\
         # Also, counts the number of clicks of each key and button.

7. Drawing Text
[answer]:  Create font obj, create some text, put text on a screen.
           font = pygame.font.SysFont("monospace", 30)
           label = font.render(<str>, (r, g, b)); color tuple
           #render(text, antialias, color, background=None)
           # antialias = True means smooth edges
           # background = (R,B,G) background color or None for transparent
           screen.blit(label, (x,y))
           Note:  screen.blit puts a text overlay over the defined <screen>

8. When to use frameworks in the real world\
    -->  See the Hang Man Game (below)


QUIZ:
    1. What f(x0 must be called so that PyGame will work in your program?
    [Answer]:  pygame.init()

    2. What f(x0 tells PyGame to reveal what has been drawn?
    [Answer]: pygame.display.update()

    3.  What f(x) is used to get all the input the user has given the program?
    [Answer]: pygame.event.get()


EXCERCISE:
    [1]  Now that you know how colors are created in PyGame, create a display
        that shows all the colors availqable to us.  It should cycle through
        all colors auotmoatically.  Remember there are three numbers that
        create a color, so you'll need to cylce through them all, in all
        combinations, to see all the colors.  Also, remeber to make the game
        easy to close by listening for user input.
        [Answer]:  see ColorReview()

Created on Tue May 26 09:59:13 2020

@author: Lifygen

"""
import pygame
# 3. Create screens in Pygame
def ch21_lesson31():
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((400,400))
    # Opens a window that should blink on and automatically close.
    # On my Win10 system it comes on and stays-on but states:
    # "Not Responding" in the windows header.  I can kill it by clicking
    # on the [x] in the upper rt. corner.


def ch21_lesson32():
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((400,300))
    while True:
        pass
    # This responds the same as ch21_lesson31().  HOwever, it is supposed
    # to keep the screen up instead of blinking on/off one time.  However,
    # the window dsiplays "Not Responding" in the window header.
    # Upon research, this is a normal behavour.  The correction is to put
    # in a program loop to keep the window up and check for keyboard/mouse
    # input to check for user action or "QUIT" selection.  See, the
    # ch21_lesson61 and ch21_lesson62 below.


def ch21_lesson61():
    import pygame
    import sys
    from pygame.locals import QUIT
    pygame.init()
    screen = pygame.display.set_mode((400,300))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


def ch21_lesson62():
    #StackOverflow solution example for handling window "Not Responding"
    import pygame
    pygame.init()
    pygame.display.set_mode((640, 480))  # opens the display
    # Note:  works without importing "QUIT" from "pygame.locals"
    # The while loop that will keep your display up and running!
    while True:
        # The for event loop, keeps track of events
        for event in pygame.event.get():
            # Keep track of pygame.QUIT selection, which is the [X] at the
            # upper right of the window header.
            if event.type == pygame.QUIT:
                # stops pygame
                pygame.quit()


# The folloiwng is part of ch21_lesson4_circle lesson:
# Define global color using for 'RED; using an
# RGB tuple (red, green, blue).
RED = (255, 0, 0)

def ch21_lesson4_circle():
    import pygame
    import sys
    # from pygame.locals import *
    pygame.init()
    # Draw a circle shape
    screen = pygame.display.set_mode((640, 480))
    pygame.draw.circle(screen, RED, (20,20), 10)
    pygame.display.update()
    print(RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("Normal Exit initiated by user.")


def ch21_lesson4_circleMove():
    import pygame
    import sys
    # from pygame.locals import *
    pygame.init()
    # Draw a circle shape
    screen = pygame.display.set_mode((640, 480))
    # Initialize the center of the circle
    x = 20
    y = 20
    pygame.draw.circle(screen, RED, (x,y), 10)
    pygame.display.update()
    print(RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("Normal Exit initiated by user.")
            x += 1
            pygame.draw.circle(screen, RED, (x,y), 10)
            if x >= 640:
                y += 20
                x = 20
            pygame.display.update()

def ch21_lesson4_circleMove2():
    import pygame
    import sys
    # from pygame.locals import *
    pygame.init()
    # Draw a circle shape
    screen = pygame.display.set_mode((640, 480))
    # Initialize the center of the circle
    x = 20
    y = 20
    pygame.draw.circle(screen, RED, (x,y), 10)
    pygame.display.update()
    print(RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("Normal Exit initiated by user.")
            pygame.draw.circle(screen, (0,0,0), (x,y), 10)
            x += 1
            pygame.draw.circle(screen, RED, (x,y), 10)
            if x >= 660:
                y += 20
                x = 20
            pygame.display.update()


def ch21_lesson4_circleMove_w_BkgndFill():
    import pygame
    import sys
    # from pygame.locals import *
    pygame.init()
    # Create named Colors
    RED = (255, 0, 0)
    Bkgnd = (80, 200, 35)
    # Define the screen size
    screen = pygame.display.set_mode((640, 480))
    # Blank the screen with new background color
    screen.fill(Bkgnd)
    # Draw a circle shape
    # Initialize the center of the circle
    x = 20
    y = 20
    pygame.draw.circle(screen, RED, (x,y), 10)
    pygame.display.update()
    print(RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("Normal Exit initiated by user.")
            x += 1
            screen.fill(Bkgnd)
            pygame.draw.circle(screen, RED, (x,y), 10)
            if x >= 640:
                y += 20
                x = 20
            pygame.display.update()


def ch21_lesson4_rectMove_w_redraw():
    # Moves a rectangle across the screen and then down one row upon reaching
    # the end of the row.
    # a) Moves when the mouse is moved.
    # b) Erases the rectangle when the [1] key is depresed
    # c) Wipes the screen when the [2] key is depressed
    import pygame
    import sys
    # from pygame.locals import *
    pygame.init()
    # Create named Colors
    RED = (255, 0, 0)
    Bkgnd = (80, 200, 35)
    # Define the screen size
    screen = pygame.display.set_mode((640, 480))
    # Blank the screen with new background color
    screen.fill(Bkgnd)
    # Draw a rectangle shape
    # Initialize rectangle
    step = 20
    xStart = 0; yStart = 0
    x = xStart; y = yStart
    width = 20; height = 20
    pygame.draw.rect(screen, RED, (x,y,width,height))
    pygame.draw.rect(screen, (15, 25, 180),(130,20,150,40))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("Normal Exit initiated by user.")
            elif pygame.key.get_pressed()[pygame.K_1]:
            # Erase last drawn object
                pygame.draw.rect(screen, Bkgnd, (x, y, width, height))
                pygame.display.update()
                print("Erase: ", x, y, width, height)
            elif pygame.key.get_pressed()[pygame.K_2]:
            # Erase the whole screen
                screen.fill(Bkgnd)
                pygame.display.update()
            elif event.type == pygame.MOUSEMOTION:
                print(event)
                # Erase the last drawn object
                pygame.draw.rect(screen, Bkgnd, (x, y, width, height))
                pygame.display.update()
                print("Bkgnd: ", x, y, width, height)
                # Re-draw the object moved over a little
                x += 5
                if x >= 640:
                    x = xStart
                    y += step
                    if y>=480:
                        y = yStart
                pygame.draw.rect(screen, RED, (x, y, width, height))
                pygame.display.update()
                print("RED: ", x, y, width, height)


def ch21_lesson4_rectMove_w_1n2Keys():
    import pygame
    import sys
    # from pygame.locals import *
    pygame.init()
    # Create named Colors
    RED = (255, 0, 0)
    Bkgnd = (80, 200, 35)
    # Define the screen size
    screen = pygame.display.set_mode((640, 480))
    # Blank the screen with new background color
    screen.fill(Bkgnd)
    # Draw a rectangle shape
    # Initialize upper rt.corner
    x = 20; y = 20
    # Initialize lower left.corner
    width = 20; height = 20
    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("Normal Exit initiated by user.")
            # Erase the image if [1] key is depressed
            if pygame.key.get_pressed()[pygame.K_1]:
                pygame.draw.rect(screen, Bkgnd, (x, y, width, height))
                pygame.display.update()
                print("Bkgnd: ", x, y, width, height)
            # Draw the image if [2] key is depressed
            elif pygame.key.get_pressed()[pygame.K_2]:
                x += 1
                if x >= 640:
                    y += 20
                    x = 20
                pygame.draw.rect(screen, RED, (x, y, width, height))
                pygame.display.update()
                print("RED: ", x, y, width, height)


def printText(myStr):
    # Print text fed to me.
    import pygame
    import sys
    pygame.init()
    # "herbert" is used in place of "screen"
    screen = pygame.display.set_mode((400, 300))
    screen.fill((10, 50, 200))
    pygame.display.update()
    fonts = pygame.font.get_fonts()
    font = fonts.pop()
    while fonts:
        try:
            new_font = pygame.font.SysFont(font, 30)
        except:
            pass
        text = new_font.render((font + "\n" + myStr), 1, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(text, (40, 40))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("Normal Exit initiated by user.")
            elif event.type == pygame.KEYDOWN:
                font = fonts.pop()


def peruseFonts(myStr):
    # Print text fed to me.
    import pygame
    import sys
    pygame.init()
    # "herbert" is used in place of "screen"
    screen = pygame.display.set_mode((800, 600))
    screen.fill((100, 150, 200))
    pygame.display.update()
    fonts = pygame.font.get_fonts()
    fonts.sort(reverse = True)
    i = 1
    imax = len(fonts) - 1
    font = fonts[i]
    while True:
        try:
            new_font = pygame.font.SysFont(font, 30)
        except:
            pass
        text = new_font.render((font + "     " + myStr), 1, (0, 0, 0))
        nextText = new_font.render(myStr, 1, (0, 0, 0))
        screen.fill((100, 150, 200))
        screen.blit(text, (40, 40))
        screen.blit(nextText, (40,120))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("Normal Exit initiated by user.")
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_PAGEUP, pygame.K_UP, 280, 273):
                    i += 1
                    if i > imax:
                        i = 0
                    font = fonts[i]
                elif event.key in (pygame.K_PAGEDOWN, pygame.K_DOWN, 281, 274):
                    i -= 1
                    if i < 0:
                        i = imax
                    font = fonts[i]

            print(font, event)


"""
# ****************************************************************************
# *** HANGMAN PROGRAM ***   ***   ***   ***   ***   ***   ***   ***   ***  ***
# ****************************************************************************
"""
import pygame
import os
import sys
from random import choice
# Global Color Pallette (R,G,B)
RED = (255,0,0)
REDCRAYON = (139, 0, 0)
ORANGE = (255,97,3)
YELLOW = (255,255,0)
GREEN = (48,128,20)
BLUE = (0,0,255)
INDIGO = (75,0,130)
PURPLE = (128,0,128)
VIOLET = (238, 130, 238)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (169, 169, 169)
GRAY = (128, 128, 128)
LIME = (0, 255, 0)
CYAN = (0, 255, 255)


def draw_gallows(screen):
    # Bottom
    pygame.draw .rect(screen, PURPLE, (450, 350, 100, 10))
    # Support post
    pygame.draw.rect(screen, PURPLE, (495, 250, 10, 100))
    # Crossbar
    pygame.draw.rect(screen, PURPLE, (450, 250, 50, 10))
    # Noose
    pygame.draw.rect(screen, PURPLE, (450, 250, 10, 25))


def draw_word(screen, letters):
    # For every letter in the word a line is drawn on screen
    # Start postion of first dash (aka letter placheholder)
    x = 10
    for i in range(letters):
        pygame.draw.line(screen, YELLOW, (x, 350),(x+20, 350), 3)
        # Spacing between dashes (letter placeholders)
        x += 30


def draw_letter(screen, font, word, guess):
    # Draw a letter over the dashed space,
    # if the guess matches a letter in the word.

    # Start postion of first dash (aka letter placheholder)
    pos = 10
    space = 30

    for letter in word:
        # If the letter matches the guess then print letter at the matching
        # location.
        if letter == guess:
            letter = font.render(letter, 3, (255,255,255))
            screen.blit(letter, (pos, 300))
        # Spacing between dashes (letter placeholders)
        pos += space


def draw_man(screen, body_part):
    # Draw the stick figure, one body part at a time.
    if body_part == "head":
        pygame.draw.circle(screen, RED, (455, 270), 10)
    if body_part == "body":
        pygame.draw.line(screen, RED, (455, 280),(455, 320), 3)
    if body_part == "leftArm":
        pygame.draw.line(screen, RED, (455, 300),(445, 285), 3)
    if body_part == "rtArm":
        pygame.draw.line(screen, RED, (455, 300),(465, 285), 3)
    if body_part == "leftLeg":
        pygame.draw.line(screen, RED, (455, 320),(445, 330), 3)
    if body_part == "rtLeg":
        pygame.draw.line(screen, RED, (455, 320),(465, 330), 3)


def get_words():
    path = os.getcwd()
    f = open(path+"/data/words.txt")
    temp = f.readlines()
    words = []
    for word in temp:
        words.append(word.strip())
    return words

def get_ch_alphaPuncKeys():
    path = os.getcwd()
    f = open(path+"/data/pygame_ch_alphaPuncKeys.txt")
    temp = f.readlines()
    keyList = []
    for key in temp:
        # Do not strip " " or else a a <space> will become a NULL string
        keyList.append(key.strip("\n"))
    return keyList


def HangMan():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    font = pygame.font.SysFont("monospace", 30)
    draw_gallows(screen)
    #draw_man(screen, body_part="head")

    words = get_words()
    word = choice(words)
    print(words)
    print(word, len(word))

    draw_word(screen, len(word))
    pygame.display.update()

    body = ['rtLeg', 'leftLeg', 'rtArm', 'leftArm', 'body', 'head']
    keyList = get_ch_alphaPuncKeys()

    while body:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if chr(event.key) in keyList:
                    guess = event.unicode
                    if guess in word:
                        draw_letter(screen, font, word, guess)
                        pygame.display.update()
                    else:
                        body_part = body.pop()
                        draw_man(screen, body_part)
                        pygame.display.update()
                        print(len(body))
                        if len(body) == 0:
                            msg = " You lost ! (}:o(~ "
                            font = pygame.font.SysFont("arial", 30, bold=True)
                            letter = font.render(msg, True,
                                                 (140,10,10), (10,128,127))
                            screen.blit(letter, (40, 40))
                            pygame.display.update()
    pygame.time.wait(10000)
    pygame.quit()
    sys.exit()


def ColorReview():
    """Displays all colors availqable to pygame us.  It shoulbcycle through
        all colors auotmoatically.  Remember there are three numbers that
        create a color, so you'll need to cylce through them all, in all
        combinations, to see all the colors.  Also, remeber to make the game
        easy to close by listening for user input.
        Same code as "ShowColors.py".
    """
    import pygame
    import sys
    from datetime import datetime

    # Initialize
    pygame.init()
    startTime = datetime.now()
    xMax = 1370
    yMax = 735
    width = 5
    height = 6
    pageMax = int(xMax * yMax / (width * height))
    screen = pygame.display.set_mode((xMax, yMax))
    screen.fill((0, 0, 0))
    pygame.display.update()
    R = 0; G = 0; B = 0
    myColors = []
    i = 0
    x = 0
    y = 0

    # Generate all color codes
    for R in range(256):
        for G in range(256):
            for B in range(256):
                myColors.append((R, G, B))
                i += 1
    print('Finished base Colors!!!')

    # Print color blocks to the screen
    for i in range(0, len(myColors)):
        color = myColors[i]
        x += width
        if x > xMax:
            x = 0
            y +=height
            if y >= yMax - height:
                y = 0
#        if (y== 0) and (x==0):
        if not x:
        # Print a line at a time to the screen
            pygame.display.update()
        #if (not y and not x):
        # Pause 1/2 a sec once a whole screen is completely printed
        #    pygame.time.wait(500)
        # print('Waiting 1/2 sec, color:'+ str(i) + ', y:' + str(y).strip('.0') +
        #       '  Row: ' + str((y/height)%(yMax/height)), i%pageMax)
        pygame.draw.rect(screen, color, (x, y, width, height))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                endTime = datetime.now()
                print("StartTime: " + startTime.strftime('%m/%d/%Y  %H:%M:%S'),
                      "   EndTime = ", endTime.strftime('%m/%d/%Y  %H:%M:%S')
                      )
                sys.exit("Normal Exit initiated by user.")
    endTime = datetime.now()
    print("StartTime: "+ startTime.strftime('%m/%d/%Y  %H:%M:%S'),
          "   EndTime = ", endTime.strftime('%m/%d/%Y  %H:%M:%S')
          )
    pygame.quit()
    sys.exit("Normal Exit Programm completed execution.")



if __name__ == "__main__":
    # Lesson 6.1
    #ch21_lesson61()
    # Lesson 6.2 works cleanly
    #ch21_lesson62()
    # Test moving objects
    #ch21_lesson4_circle()
    #ch21_lesson4_circleMoveImproved()
    #ch21_lesson4_rectMove_w_redraw()
    # Shows a font per page; allow user to peruse up and down through the list
    #peruseFonts("Check out this font!")
    pass
    # HangMan()
    # peruseFonts("Check out this font!").
ColorReview()