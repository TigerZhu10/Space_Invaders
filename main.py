import pygame, sys
from settings import Settings

pygame.init()
# 创建Object给
Game_settings = Settings()


screen = pygame.display.set_mode((Game_settings.WINDOW_WIDTH, Game_settings.WINDOW_HEIGHT))
pygame.display.set_caption("Space Invader!")

def Game_runner():
    game_running = True
    while game_running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()

        screen.fill(Game_settings.bg_color)

        pygame.display.flip()




Game_runner()