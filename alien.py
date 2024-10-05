import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("./assets/images/alien.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = 600
        self.rect.centery = 400


    def display_alien(self):
        self.screen.blit(self.image, self.rect)

        
        