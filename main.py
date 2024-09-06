import pygame, sys
from settings import Settings
from ship import Ship

pygame.init()
# 创建Object给Game_settings
Game_settings = Settings()
Alien_ship = Ship("alien.png", Game_settings.WINDOW_WIDTH//2, Game_settings.WINDOW_HEIGHT//2)




screen = pygame.display.set_mode((Game_settings.WINDOW_WIDTH, Game_settings.WINDOW_HEIGHT))
pygame.display.set_caption("Space Invader!")

def Game_runner():
    game_running = True
    while game_running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()

        screen.fill(Game_settings.bg_color)

        screen.blit(Alien_ship.image, Alien_ship.rect)
        

        pygame.display.flip()


Game_runner()