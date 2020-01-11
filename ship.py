import pygame
from settings import Settings
class Ship():
    def __init__(self,screen):
        self.screen=screen
        self.image = pygame.image.load("images/plane.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect();
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    moving_right = False
    moving_left = False
    def update(self):
        if self.moving_right:
            if centerx+100< :
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1
