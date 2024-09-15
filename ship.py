import pygame

'''
@Object:
关于飞船的属性和干的事情放在这个类
'''
class Ship:
    def __init__(self, display_screen, game_settings):
        self.game_settings = game_settings
        self.screen = display_screen
        self.ship_image = pygame.image.load("./assets/images/player_ship.png")
        self.ship_image_rect = self.ship_image.get_rect()
        self.ship_image_rect.centerx = self.game_settings.WINDOW_WIDTH//2
        self.ship_image_rect.bottom = self.game_settings.WINDOW_HEIGHT

        self.moving_right = False
        self.moving_left = False

    def moving_ship(self):
        if self.moving_right and self.ship_image_rect.right <= self.game_settings.WINDOW_WIDTH:
            self.ship_image_rect.centerx += 1
        if self.moving_left and self.ship_image_rect.left >= 0:
            self.ship_image_rect.centerx -= 1

    def display_ship(self):
        self.screen.blit(self.ship_image, self.ship_image_rect)


