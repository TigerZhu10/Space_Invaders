import pygame

'''
@Object:
关于飞船的属性和干的事情放在这个类
'''
class Ship:
    def __init__(self, display_screen):
        self.screen = display_screen
        self.ship_image = pygame.image.load("./assets/images/player_ship.png")
        self.ship_image_rect = self.ship_image.get_rect()
        self.ship_image_rect.center = (500, 600)

    def display_ship(self):
        self.screen.blit(self.ship_image, self.ship_image_rect)













        # screen.blit(Alien_ship.image, Alien_ship.rect)
        # self.image = pygame.image.load(image)
        # self.rect = self.image.get_rect()
        # self.rect.center = (x, y)


