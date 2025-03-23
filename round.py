import pygame

class Round():
    def __init__(self, display_screen, game_settings, rou):
        self.screen = display_screen
        self.rou = rou
        self.game_settings = game_settings

        round_font = pygame.font.SysFont('calibri', 30)

        self.round_text = round_font.render(rou, True, (227, 245, 66))
        self.round_text_rect = self.round_text.get_rect()
        self.round_text_rect.topright = (game_settings.WINDOW_WIDTH - 40, 45)

    def display_round(self):
        self.screen.blit(self.round_text, self.round_text_rect)