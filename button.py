import pygame

class Button():
    def __init__(self, display_screen, game_settings, msg):
        self.game_settings = game_settings
        self.screen = display_screen
        self.msg = msg

        self.button_font = pygame.font.SysFont('calibri', 30)

        # give screen a rect plot the coordinates in center and than give it to self.rect
        self.screen_rect = display_screen.get_rect()
        self.rect = pygame.Rect(self.game_settings.button_attributes)
        self.rect.center = self.screen_rect.center

        self.button_text = self.button_font.render(self.msg, True, (227, 245, 66))
        self.button_text_rect = self.button_text.get_rect()
        self.button_text_rect.center = (self.rect.centerx, self.rect.centery)

    def draw_buttons(self):
        pygame.draw.rect(self.screen, self.game_settings.button_color, self.rect)
    
    def display_text(self):
        self.screen.blit(self.button_text, self.button_text_rect)