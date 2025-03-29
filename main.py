import pygame
from settings import Settings
import game_functions          
from ship import Ship
from button import Button
from pygame.sprite import Group
from score import Score
from lives import Lives
from round import Round
from sound import Sound

pygame.init()   
# Game_settings Object that contains every attributes and method 
game_settings = Settings()

FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((game_settings.WINDOW_WIDTH, game_settings.WINDOW_HEIGHT))
pygame.display.set_caption("Space Invader!")

bullet_group = Group()
alien_group = Group()

button = Button(screen, game_settings, "play") 
player_ship = Ship(screen, game_settings)


game_functions.create_alien_group(game_settings, screen, alien_group, player_ship, bullet_group)


def Game_runner():
    game_running = True 
    while game_running:
        clock.tick(FPS)

        sound = Sound(screen, "./assets/sounds/new_round.wav", "./assets/sounds/alien_fire.wav", "./assets/sounds/player_hit.wav", "./assets/sounds/alien_hit.wav")
        round= Round(screen, game_settings, "Round: " + str(game_settings.round))
        score = Score(screen, game_settings, "Score: " + str(game_settings.score))
        lives = Lives(screen, game_settings, "Lives: " + str(game_settings.lives))

        game_functions.check_mouse_key_events(player_ship, screen, bullet_group, game_settings, button)
        game_functions.update_screen(screen, player_ship, game_settings, bullet_group, alien_group, button, score, lives, round)
Game_runner()