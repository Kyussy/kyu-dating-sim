import pygame
import sys
from time import sleep

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame window ig")
while True:
    # make text that says "Hello world!"
    font = pygame.font.Font(None, 30)
    text = font.render(
        "Wow look at this very long dialouge i sure hope it doesnt go off screen",
        1,
        (255, 255, 255),
    )
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    textpos.centery = screen.get_rect().centery - 145
    screen.blit(text, textpos)
    # create a rectangle that is hollow and white
    pygame.draw.rect(screen, (255, 255, 255), (50, 10, 500, 100), 3)
    # update the display
    pygame.display.update()
    # loop through the events
    for event in pygame.event.get():
        # quit if the quit button was pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
