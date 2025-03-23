import pygame

class Score():
    def __init__(self, display_screen, game_settings, scr):
        self.screen = display_screen
        self.scr = scr
        self.game_settings = game_settings

        score_font = pygame.font.SysFont('calibri', 30)

        self.score_text = score_font.render(scr, True, (227, 245, 66))
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.topleft = (10, 10)

    def display_score(self):
        self.screen.blit(self.score_text, self.score_text_rect)