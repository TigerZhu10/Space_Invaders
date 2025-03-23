import pygame

class Lives():
    def __init__(self, display_screen, game_settings, liv):
        self.screen = display_screen
        self.liv = liv
        self.game_settings = game_settings

        lives_font = pygame.font.SysFont('calibri', 30)

        self.lives_text = lives_font.render(liv, True, (227, 245, 66))
        self.lives_text_rect = self.lives_text.get_rect()
        self.lives_text_rect.topright = (game_settings.WINDOW_WIDTH - 40, 13)

    def display_lives(self):
        self.screen.blit(self.lives_text, self.lives_text_rect)