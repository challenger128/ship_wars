import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Class for working with our bullets
    """
    def __init__(self, screen, game_setting, ship):
        """
        Init bullet which inherited by Sprite.
        We will use Group() for make bullet manipulation simpler
        :param screen: required for output our bullet
        :param game_setting: required for bullet setting
        :param ship: required for bullet position
        """
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('ship_wars/assets/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.speed = game_setting.bullet_speed

    def update(self):
        """
        Updates bullet position
        :return: None
        """
        self.rect.y -= self.speed

    def blit(self):
        """
        Draws simple rectangle which is the bullet
        :return: None
        """
        self.screen.blit(self.image, self.rect)