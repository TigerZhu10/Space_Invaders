import pygame
'''
@Object:
关于飞船的属性和干的事情放在这个类
'''
class Ship:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
