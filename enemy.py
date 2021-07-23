import pygame
from random import randint
from pygame.sprite import Sprite


class EnemyShip(Sprite):

    def __init__(self, screen, game_setting):
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
        return self.rect.right >= self.screen_rect.right or self.rect.left <=0

    def update(self):
        self.rect.centerx += self.game_setting.enemy_direction * self.speed

    def blit(self):
        self.screen.blit(self.image, self.rect)