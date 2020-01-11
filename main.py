import sys
import pygame as p
import time
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    #初始化游戏，并创建屏幕
    p.init()
    ai_settings = Settings()
    screen = p.display.set_mode((ai_settings.screen_height,ai_settings.screen_width))
    p.display.set_caption("Alien Invalid")
    ship = Ship(screen)
    while True:
        gf.check_events()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        p.display.flip()
run_game()
    
`
