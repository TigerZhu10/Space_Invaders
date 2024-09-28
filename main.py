import pygame
from settings import Settings
import game_functions        
from ship import Ship
from bullet import Bullet

pygame.init()
# Game_settings 得到了Settings里的所有东西(属性和方式)
game_settings = Settings()

screen = pygame.display.set_mode((game_settings.WINDOW_WIDTH, game_settings.WINDOW_HEIGHT))
pygame.display.set_caption("Space Invader!")

#bullet_group = pygame.sprite.Group()
player_ship = Ship(screen, game_settings)
bullet = Bullet(screen, player_ship, game_settings)

def Game_runner():
    game_running = True
    while game_running:
        game_functions.check_mouse_key_events(player_ship, bullet)
        game_functions.update_screen(screen, player_ship, game_settings, bullet)



Game_runner()