import pygame, sys

def check_mouse_key_events(ship):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()
            
        #当按键被按下的时候把flag变成True来连续移动飞船
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif ev.key == pygame.K_LEFT:
                ship.moving_left = True

        #当按键松开的时候把flag重新变为false来停止移动         
        elif ev.type == pygame.KEYUP:
            if ev.key == pygame.K_RIGHT:
                ship.moving_right = False
            if ev.key == pygame.K_LEFT:
                ship.moving_left = False


    
    

def update_screen(display_screen, ship, game_settings):
        display_screen.fill(game_settings.bg_color)

        ship.moving_ship()

        ship.display_ship()
        
        # 更新所有活动
        pygame.display.flip()
