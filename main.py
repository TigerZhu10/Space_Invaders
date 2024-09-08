import pygame
from settings import Settings
import game_functions
from ship import Ship

pygame.init()
# Game_settings 得到了Settings里的所有东西(属性和方式)
Game_settings = Settings()


screen = pygame.display.set_mode((Game_settings.WINDOW_WIDTH, Game_settings.WINDOW_HEIGHT))
pygame.display.set_caption("Space Invader!")

Alien_ship = Ship(screen)

def Game_runner():
    game_running = True
    while game_running:
        game_functions.check_mouse_key_events()
        game_functions.update_screen(screen, Alien_ship, Game_settings)



Game_runner()