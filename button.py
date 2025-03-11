import pygame

class Button():
    def __init__(self, display_screen, game_settings):
        self.game_settings = game_settings
        self.screen = display_screen

        # give screen a rect plot the coordinates in center and than give it to self.rect
        self.screen_rect = display_screen.get_rect()
        self.rect = pygame.Rect(self.game_settings.button_attributes)
        self.rect.center = self.screen_rect.center

    def draw_buttons(self):
        pygame.draw.rect(self.screen, self.game_settings.button_color, self.rect)