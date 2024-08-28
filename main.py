import pygame, sys
from setting import Game_Settings


pygame.init()
setting = Game_Settings()
screen = pygame.display.set_mode((setting.WINDOW_WIDTH, setting.WINDOW_HEIGHT))
pygame.display.set_caption("Alien coming")


def run_game():
    game_running = True
    while game_running:
        # 监控键盘和鼠标的事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(setting.bg_color)

        pygame.display.flip()


run_game()
