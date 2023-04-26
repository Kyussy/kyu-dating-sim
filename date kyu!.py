print("this game was made entirely by kyu, the narcisistic fuck he is, enjoy!")
from PyQt5.QtWidgets import *
import pygame
import questin
from time import sleep
pygame.init()
win = pygame.display.set_mode((400,400))
fps = pygame.time.Clock()
run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    questin.question_box(["kyu be asking yo ass", "Yes.", "No."], [questin.end, questin.end])
    pygame.display.update()
    fps.tick(60)
