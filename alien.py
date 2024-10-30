import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, screen, alien_group, game_settings):
        super().__init__()
        self.alien_group = alien_group
        self.game_settings = game_settings

        self.screen = screen
        self.image = pygame.image.load("./assets/images/alien.png")
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = self.rect.height


        self.alien_velocity = 1

    def update(self):
        self.alien_move()

    def alien_move(self):

        if self.rect.right < self.game_settings.WINDOW_WIDTH:
            self.rect.x += self.game_settings.alien_velocity
        
        if self.rect.right == self.game_settings.WINDOW_WIDTH:
            self.rect.bottom += 1

       

         
        


    def display_alien(self):
        self.screen.blit(self.image, self.rect)
    
    
        
        