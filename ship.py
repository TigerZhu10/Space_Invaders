import pygame


'''
@Object:
The attributes and things to do about the ship are placed in this class.
'''
class Ship:
    def __init__(self, display_screen, game_settings):
        self.game_settings = game_settings
        self.screen = display_screen
        self.image = pygame.image.load("./assets/images/player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = self.game_settings.WINDOW_WIDTH//2
        self.rect.bottom = self.game_settings.WINDOW_HEIGHT

        self.moving_right = False
        self.moving_left = False

        self.position = float(self.rect.centerx)

    def moving_ship(self):
        if self.moving_right and self.rect.right <= self.game_settings.WINDOW_WIDTH:
            self.position += self.game_settings.ship_velocity
        if self.moving_left and self.rect.left >= 0:
            self.position -= self.game_settings.ship_velocity

        self.rect.centerx = self.position

    def display_ship(self):
        self.screen.blit(self.image, self.rect)


