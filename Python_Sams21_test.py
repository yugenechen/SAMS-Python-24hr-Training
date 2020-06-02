def Hello():
    print("hello")



if __name__ == "__main__":
    #HangMan()
    pass
import pygame
import os
import sys

pygame.init()

startRow = 20
startPos = 10
spacing = 20
width = 600; height = 400

charPos = startPos
lineNum = startRow

screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("monospace", 30)
screen.fill((128,128,128))
pygame.display.update()


# render(text, antialias, color, background=None)
label = font.render("Hello Yu-Gene!!!", False, (0, 128, 0),(128, 0 , 0))
screen.blit(label, (10,30))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
