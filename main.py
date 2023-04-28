import pygame
from pygame.locals import *
from pygame import *
import sys
from time import sleep

from data.renderText import renderText

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Dating sim")

lineid = 0

pygame.draw.rect(screen, (255, 255, 255), (50, 10, 500, 100), 3)

# read the text from the file
with open("data/script.txt", "r") as f:
    texttowrite = f.readlines()

texttowrite = [x.strip() for x in texttowrite]

renderText(screen, texttowrite, lineid)

lineid += 1

while True:

    pygame.display.update()

    # loop through the events
    for event in pygame.event.get():
        # quit if the quit button was pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # check if the mouse was clicked
        if event.type == pygame.MOUSEBUTTONDOWN:

            if lineid > len(texttowrite) - 1:
                lineid = 0

            renderText(screen, texttowrite, lineid)

            lineid += 1

            pygame.display.update()
