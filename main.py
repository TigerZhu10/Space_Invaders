import pygame, sys
from settings import Settings
from ship import Ship

pygame.init()
# Game_settings 得到了Settings里的所有东西(属性和方式)
Game_settings = Settings()
# Alien_ship = Ship("alien.png", Game_settings.WINDOW_WIDTH//2, Game_settings.WINDOW_HEIGHT//2)




screen = pygame.display.set_mode((Game_settings.WINDOW_WIDTH, Game_settings.WINDOW_HEIGHT))
pygame.display.set_caption("Space Invader!")

Alien_ship = Ship(screen)

def Game_runner():
    game_running = True
    while game_running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()

        screen.fill(Game_settings.bg_color)
        
        Alien_ship.display_ship()
        
        # 更新所有活动
        pygame.display.flip()


Game_runner()