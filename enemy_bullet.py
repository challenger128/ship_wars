import pygame
from pygame.sprite import Sprite


class EnemyBullet(Sprite):
    """
    Class for working with our bullets
    """
    def __init__(self, screen, game_setting, enemy):
        """
        Init bullet which inherited by Sprite.
        We will use Group() for make bullet manipulation simpler
        :param screen: required for output our bullet
        :param game_setting: required for bullet setting
        :param enemy: required for bullet position
        """
        super(EnemyBullet, self).__init__()
        self.screen = screen
        self.enemy = enemy
        self.image = pygame.image.load('ship_wars/assets/enemy_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = enemy.rect.centerx
        self.rect.bottom = enemy.rect.bottom
        self.speed = game_setting.enemy_bullet_speed

    def update(self):
        """
        Updates bullet position
        :return: None
        """
        self.rect.y += self.speed

    def blit(self):
        """
        Draws simple rectangle which is the bullet
        :return: None
        """
        self.screen.blit(self.image, self.rect)