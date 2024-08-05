import pygame, sys
from setting import Settings


pygame.init()
game_setting = Settings()
screen = pygame.display.set_mode(game_setting.WINDOW_HEIGHT, game_setting.WINDOW_WIDTH)
pygame.display.set_caption("Alien coming")


def run_game():
    game_running = True
    while game_running:
        # 监控键盘和鼠标的事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(game_setting.bg_color)

        pygame.display.flip()


run_game()
