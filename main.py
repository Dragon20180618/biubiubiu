import sys
import pygame as p
import time
from settings import Settings
from ship import Ship
def run_game():
    #初始化游戏，并创建屏幕
    p.init()
    ai_game = Settings()
    screen = p.display.set_mode((ai_game.screen_height,ai_game.screen_width))
    p.display.set_caption("Alien Invalid")
    ship = Ship(screen)
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                sys.exit()
        screen.fill(ai_game.bg_color)
        ship.blitme()
        p.display.flip()
run_game()
