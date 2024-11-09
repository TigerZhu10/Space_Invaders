import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, screen, alien_group, game_settings, alien_position_x, alien_position_y, bullet_group):
        super().__init__()
        self.alien_group = alien_group
        self.game_settings = game_settings
        self.bullet_group = bullet_group

        self.screen = screen
        self.image = pygame.image.load("./assets/images/alien.png")
        self.rect = self.image.get_rect()

        self.rect.x = alien_position_x
        self.rect.y = alien_position_y


        self.alien_position = float(self.rect.x)                                                                                                                                                                              

    def update(self):
        self.alien_move()
        self.check_collisions()

    def alien_move(self):

        self.alien_position += self.game_settings.alien_velocity * self.game_settings.alien_direction
        self.rect.x = self.alien_position

        self.check_edge()

    def check_edge(self):

        if self.rect.right >= self.game_settings.WINDOW_WIDTH or self.rect.left <= 0:
            self.game_settings.alien_direction *= -1
            for alien in self.alien_group.sprites():
                alien.rect.y += self.game_settings.alien_drop_speed

    def check_collisions(self):
        pygame.sprite.groupcollide(self.bullet_group, self.alien_group, True, True)




    def display_alien(self):
        self.screen.blit(self.image, self.rect)
    
    
        
        