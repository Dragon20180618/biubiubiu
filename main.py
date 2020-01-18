import sys
import pygame as p
import time
from settings import Settings
from ship import Ship
import game_functions as gf 
from pygame.sprite import Group
def run_game():
    #初始化游戏，并创建屏幕
    p.init()
    ai_settings = Settings()
    screen = p.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    p.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    bullets = Group()
    bullets.__init__()
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)
run_game()
