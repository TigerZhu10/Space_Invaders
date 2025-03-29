import pygame

class Sound():
    def __init__(self, new_round, alien_fire, player_hit, alien_hit):
        self.main_music = pygame.mixer.Sound(new_round)
        self.fire_music = pygame.mixer.Sound(alien_fire)
        self.player_hit_music = pygame.mixer.Sound(player_hit)
        self.alien_hit_music = pygame.mixer.Sound(alien_hit)
    
    def new_round_sound(self):
        self.main_music.play()
    
    def fire_sound(self):
        self.fire_music.play()

    def player_hit_sound(self):
        self.player_hit_music.play()

    def alien_hit_sound(self):
        self.alien_hit_music.play()