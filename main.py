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
    screen = p.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    p.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings,screen,ship)
run_game()
