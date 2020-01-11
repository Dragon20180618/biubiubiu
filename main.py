import sys
import pygame as p
import time
from settings import Settings
def run_game():
    #初始化游戏，并创建屏幕
    p.init()
    screen=p.display.set_mode((1200,800))
    p.display.set_caption("Alien Invasion")
    bg_color=(230,230,230)
    i=1
    j=1
    k=1
    while True:
        if i==230:
            i=1
            
        if k==230:
            k=1
        
        bg_color=(230,k,i)
        i+=1
        k+=1
        for event in p.event.get():
            if event.type == p.QUIT:
                sys.exit()
        screen.fill(bg_color)
        p.display.flip()
    #time.sleep
run_game()
