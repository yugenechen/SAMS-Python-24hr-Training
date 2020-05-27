# -*- coding: utf-8 -*-
"""SAMS Ch 21 Lesson Excercise
# ****************************************************************************
# *** HANGMAN PROGRAM ***   ***   ***   ***   ***   ***   ***   ***   ***  ***
# ****************************************************************************
NOTES:
    1. words.txt is in /data/ directory of the current working directory
Created on Wed May 27 09:14:54 2020

@author: Lifygen
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


if __name__ == "__main__":
    HangMan():

