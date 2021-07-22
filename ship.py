import pygame


class Ship:
    """
    Class for make ships
    """
    def __init__(self, screen):
        """
        Init our ship, loading a sprite and make a rectangle
        :param screen: requires screen where our ship will be shown
        """
        self.screen = screen
        self.image = pygame.image.load('alien_invasion/assets/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blit(self):
        """
        Draws ship in its position
        :return: None
        """
        self.screen.blit(self.image, self.rect)
