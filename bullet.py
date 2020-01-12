import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        self.screen = screen
        #create bullet at (0,0), then set the right location
        self.rect = pygame.Rect(0,0,ai_setting.bullet_width,
                                ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor
