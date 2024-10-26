import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, screen, alien_group):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("./assets/images/alien.png")
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = self.rect.height

        self.alien_velocity = 1

    def update(self):
        self.alien_move()

    def alien_move(self):
        

    def display_alien(self):
        self.screen.blit(self.image, self.rect)
    
    
        
        