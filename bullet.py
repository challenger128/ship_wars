import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

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
        self.rect = pygame.Rect(0, 0, game_setting.bullet_width,
                                game_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.color = game_setting.bullet_color
        self.speed = game_setting.bullet_speed

    def update(self):
        """
        Updates bullet position
        :return: None
        """
        self.rect.y -= self.speed

    def draw(self):
        """
        Draws simple rectangle which is the bullet
        :return: None
        """
        pygame.draw.rect(self.screen, self.color, self.rect)