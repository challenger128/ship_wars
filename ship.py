import pygame


class Ship:
    """
    Class for make ships
    """
    def __init__(self, screen, game_setting):
        """
        Init our ship, loading a sprite and make a rectangle
        :param screen: requires screen where our ship will be shown
        """
        self.screen = screen
        self.image = pygame.image.load('ship_wars/assets/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.game_setting = game_setting

    def update(self):
        """
        Update ship position
        :return: None
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.game_setting.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.game_setting.ship_speed

    def blit(self):
        """
        Draws ship in its position
        :return: None
        """
        self.screen.blit(self.image, self.rect)
