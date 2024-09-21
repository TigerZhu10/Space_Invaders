import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, display_screen, player_ship):
        super().__init__()
        self.screen = display_screen
        self.ship = player_ship
    
        self.rect = pygame.Rect(0,0,3,15)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top

        self.bullet_position = float(self.rect.y)
    def update(self):
        self.display_bullet()

    def display_bullet(self):
        pygame.draw.rect(self.screen, (0,255,0), self.rect)
        