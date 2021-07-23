import pygame
from random import randint
from pygame.sprite import Sprite


class EnemyShip(Sprite):
    """
    Class for working with enemy instants
    """
    def __init__(self, screen, game_setting):
        """
        Init an enemy
        :param screen: required for right positions
        :param game_setting: uses some presets
        """
        super(EnemyShip, self).__init__()
        self.screen = screen
        self.game_setting = game_setting
        self.image = pygame.image.load('ship_wars/assets/enemy' + str(randint(1, 2)) + '.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.rect.width
        self.rect.y = self.rect.height
        self.bullet_fired = False
        self.speed = game_setting.enemy_speed


    def check_edge(self):
        """
        Function which checks if enemy fly out
        :return:
        """
        return self.rect.right >= self.screen_rect.right or self.rect.left <=0

    def update(self):
        """
        Updates enemy position
        :return: None
        """
        self.rect.centerx += self.game_setting.enemy_direction * self.speed

    def blit(self):
        """
        Just showing enemy in main Surface (screen)
        :return: None
        """
        self.screen.blit(self.image, self.rect)