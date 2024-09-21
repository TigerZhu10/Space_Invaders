import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, display_screen, player_ship):
        super().__init__()
        self.screen = display_screen
        self.ship = player_ship

        self.Bullet_rect = pygame.Rect(0,0,3,15)
        self.Bullet_rect.centerx = self.ship.rect.centerx
        self.Bullet_rect.top = self.ship.rect.top

        #self.bullet_position = float(self.rect.y)

    def display_Bullet(self):
        pass
        