import pygame
import random
class Alien():
    def __init__(self):
        self.color = [(230,0,0),(0,230,0),(0,0,230)]
        self.image = [
            pygame.image.load("images\\green.bmp"),
            pygame.image.load("images\\yellow.bmp"),
            pygame.image.load("images\\red.bmp")
            ]
Alien()
