import pygame
from settings import Settings
import game_functions        
from ship import Ship
from pygame.sprite import Group
from alien import Alien

pygame.init() 
# Game_settings Object that contains every attributes and method 
game_settings = Settings()

screen = pygame.display.set_mode((game_settings.WINDOW_WIDTH, game_settings.WINDOW_HEIGHT))
pygame.display.set_caption("Space Invader!")

bullet_group = Group()
alien_group = Group()

player_ship = Ship(screen, game_settings)
alien = Alien(screen)


game_functions.create_alien_group(game_settings, screen, alien, alien_group)

def Game_runner():
    game_running = True
    while game_running:
        game_functions.check_mouse_key_events(player_ship, screen, bullet_group, game_settings)
        game_functions.update_screen(screen, player_ship, game_settings, bullet_group, alien_group)


Game_runner()