import pygame
from pygame.locals import *
from pygame import *
from data.drawText import drawText


def renderText(screen, texttowrite, lineid):

    screen.fill(pygame.Color("black"))

    pygame.draw.rect(screen, (255, 255, 255), (50, 10, 500, 100), 3)

    if len(texttowrite[lineid]) > 30:
        font = pygame.font.Font(None, 25)
    elif len(texttowrite[lineid]) > 60:
        font = pygame.font.Font(None, 20)
    elif len(texttowrite[lineid]) > 90:
        font = pygame.font.Font(None, 15)
    else:
        font = pygame.font.Font(None, 30)

    text = drawText(
        screen,
        texttowrite[lineid],
        (255, 255, 255),
        (60, 15, 450, 90),
        font,
    )

    text = font.render(
        text,
        1,
        (255, 255, 255),
    )
