import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, display_screen, player_ship, game_settings):
        super().__init__()
        self.game_settings = game_settings
        self.screen = display_screen
        self.ship = player_ship
    
        self.rect = pygame.Rect(self.game_settings.bullet_spot)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top

        # Turn (rect.y) to a decimal and give it to (bullet_position_x) 
        self.bullet_position_x = float(self.rect.y)
        self.bullet_move = False

    def display_bullet(self):
        self.bullet_position_x -= self.game_settings.bullet_velocity
        # return the number back to (rect.y)
        self.rect.y = self.bullet_position_x


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.game_settings.bullet_color, self.rect)
        