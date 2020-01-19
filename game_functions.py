import sys
import pygame

from bullet import Bullet
from pygame.sprite import Group

#from pygame import mixer
#mixer.init()
#mixer.music.load('music\\bullet.mp3')

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        
def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    ship.update()
    for bullet in bullets.sprites():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
        else :
            bullet.draw_bullet()
    pygame.display.flip()
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
            #mixer.music.play()
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
