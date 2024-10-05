import pygame, sys
from bullet import Bullet


def Key_up(ship, event):

    #当按键松开的时候把flag重新变为false来停止移动
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
def Key_down(ship, event, bullet_group, screen, game_settings):

    #当按键被按下的时候把flag变成True来连续移动飞船
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True 

    if event.key == pygame.K_SPACE:
        lunch_bullet(bullet_group, game_settings, screen, ship)


def check_mouse_key_events(ship, screen, bullet_group, game_settings):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()

        elif ev.type == pygame.KEYDOWN:
            Key_down(ship, ev, bullet_group, screen, game_settings)
        elif ev.type == pygame.KEYUP:
            Key_up(ship, ev)  
              

def update_screen(display_screen, ship, game_settings, bullet_group, alien):
        display_screen.fill(game_settings.bg_color)

        ship.moving_ship()
        ship.display_ship()

        alien.display_alien()

        bullet_group_display(bullet_group)
        
        # 更新所有活动
        pygame.display.flip()


def bullet_group_display(bullet_group):
    for bullet in bullet_group.sprites():
            bullet.draw_bullet()
            bullet.display_bullet()
        
    for bullet in bullet_group.copy():
        if bullet.rect.bottom <= 0:
            bullet_group.remove(bullet)

def lunch_bullet(bullet_group, game_settings, screen, ship):
        if len(bullet_group) < game_settings.bullet_num_allowed:
            bullet_group.add(Bullet(screen, ship, game_settings))