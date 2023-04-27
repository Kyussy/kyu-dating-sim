import pygame
from pygame.locals import *
from pygame import *
import sys
from time import sleep

from data.drawText import drawText

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Dating sim")

while True:
    font = pygame.font.Font(None, 30)
    # textpos = text.get_rect()
    # textpos.centerx = screen.get_rect().centerx
    # textpos.centery = screen.get_rect().centery - 145
    # screen.blit(text, textpos)

    # create a rectangle that is hollow and white
    pygame.draw.rect(screen, (255, 255, 255), (50, 10, 500, 100), 3)

    text = drawText(
        screen,
        "Omagawd it actually wraps! Could you even imagine that? I mean, I can't. I'm just crazy asf ik! What if it goes out of border? I dont think its possible but lets test :D. Not there yet! Still writing. I think this is enough.",
        (255, 255, 255),
        (60, 15, 450, 90),
        pygame.font.Font(None, int(450 * 450 / 500)),
    )

    text = font.render(
        text,
        1,
        (255, 255, 255),
    )

    pygame.display.update()

    # loop through the events
    for event in pygame.event.get():
        # quit if the quit button was pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
