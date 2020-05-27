# -*- coding: utf-8 -*-
"""pygame example - font.render()  & screen.blit() using "surface" objects
Script exploring printing Text to a Graphics Screen.
Recognizes keyboard inputs and prints them to the screen.  This example detects alphaNumerics and punctuation from the main keyboard but does not accept input
from the side keypad.

Create font obj, create some text, put text on a screen.

           font = pygame.font.SysFont("monospace", 30)
           label = font.render(<str>, (r, g, b)); color tuple
           #       font.render(<str>, <T/F>, <textcolor(R,G,B)>, <BkgndCol(R,G,B)>)
           #render(text, antialias, color, background=None)
           #    antialias = <bool>, True means smooth edges
           #    background = (R,B,G) background color or None for transparent

           screen.blit(label, (x,y))
           Note:  screen.blit puts a text overlay over the defined <screen>

font.render(<str>, <True/False>, <textcolor(R,G,B)>, <BkgndCol(R,G,B)>)
# Noe: Bkgnd left None will be clear.
screen.blit(<surface>, (charPos, lineNum)) -> <label>

Created on Wed May 27 13:36:40 2020

@author: Lifygen
"""
import pygame
import os
import sys

def get_ch_alphaPuncKeys():
    path = os.getcwd()
    f = open(path+"/data/pygame_ch_alphaPuncKeys.txt")
    temp = f.readlines()
    keyList = []
    for key in temp:
        # Do not strip " " or else a a <space> will become a NULL string
        keyList.append(key.strip("\n"))
    return keyList


if __name__ == "__main__":
    pass
pygame.init()

startRow = 20
startPos = 10
spacing = 20
lspacing = 30
width = 600; height = 400

screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("monospace", 30)

charPos = startPos
lineNum = startRow

keyList = get_ch_alphaPuncKeys()

print(keyList)
while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keypress = event.unicode
                # keypress is the letter or character.
                print("keypress = ", keypress)
                # event.key is the ASCHII code decimal value
                print("EventKey: ", event.key)
                if chr(event.key) in keyList:
                   keypress = event.unicode
                   print("keypress | keyList = ", keypress)
                   letter = keypress
                   letter = font.render(keypress, True, (255,255,255))
                   screen.blit(letter, (charPos, lineNum))
                   pygame.display.update()
                   charPos += spacing
                   if charPos > (width - spacing):
                       charPos = startPos
                       lineNum += lspacing
                       if lineNum > (height - (lspacing)):
                           lineNum = startRow
                   print("Position: ", charPos,lineNum)
    except Exception as err:
        print("Unexpected error:", sys.exc_info()[0])
        print("err.filename:  ", err.filename)
        print("err.errno:  ", err.errno)
        print("err.strerror:  ", err.strerror)
        print("err.args:  ", err.args)
        print("")
        pygame.quit()
        raise
        sys.exit()

