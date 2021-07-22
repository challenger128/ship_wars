import pygame.freetype


class Text:

    def __init__(self, screen, game_setting, text):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_setting = game_setting
        self.text = text

    def update(self, new_text):
        self.text = new_text

    def output(self):
        text_surface, rect = pygame.freetype.Font\
            ('ship_wars/assets/GameFont.TTF', 24).render(self.text, self.game_setting.text_color)
        self.screen.blit(text_surface, self.screen_rect.topleft)
