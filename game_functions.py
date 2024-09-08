
import pygame, sys

def check_mouse_key_events():
    for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()

def update_screen(display_screen, ship, game_settings):
        display_screen.fill(game_settings.bg_color)

        ship.display_ship()
        
        # 更新所有活动
        pygame.display.flip()
