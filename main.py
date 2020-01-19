import sys
import pygame as p
import time
from settings import Settings
from ship import Ship
import game_functions as gf 
from pygame.sprite import Group
from pygame import mixer

import os,time,random
from multiprocessing import Process, Queue
mixer.init()
mixer.music.load('music\\bullet.mp3')
def music():
    while True:
        print("ok")
        for event in p.event.get():
            if event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:
                    mixer.init()
                    mixer.music.load('music\\bullet.mp3')
                    mixer.play()
def run_game():
    #初始化游戏，并创建屏幕
    p.init()
    ai_settings = Settings()
    screen = p.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    p.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    bullets = Group()
    bullets.__init__()

    
    Process(target=music,args=()).start()

    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)
run_game()
