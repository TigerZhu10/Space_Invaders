import pygame, sys

def Key_up(ship, event):

    #当按键松开的时候把flag重新变为false来停止移动
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False



def Key_down(ship, event, bullet):

    #当按键被按下的时候把flag变成True来连续移动飞船
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        bullet.bullet_move = True

def check_mouse_key_events(ship, bullet):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()

        if ev.type == pygame.KEYDOWN:
            Key_down(ship, ev, bullet)
        if ev.type == pygame.KEYUP:
            Key_up(ship, ev)  
              

def update_screen(display_screen, ship, game_settings, bullet):
        display_screen.fill(game_settings.bg_color)

        ship.moving_ship()

        ship.display_ship()

        bullet.draw_bullet()

        bullet.display_bullet()
        
        # 更新所有活动
        pygame.display.flip()
