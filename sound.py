import pygame

class Sound():
    def __init__(self, display_screen, new_round, alien_fire, player_hit, alien_hit):
        self.screen = self.display_screen
        self.main_music = pygame.mixer.Sound(new_round)
        self.fire_music = pygame.mixer.Sound(alien_fire)
        self.player_hit_music = pygame.mixer.Sound(player_hit)
        self.alien_hit_music = pygame.mixer.Sound(alien_hit)
    
    def display_sound(self):
        