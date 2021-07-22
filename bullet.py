import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, screen, game_setting, ship):

        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, game_setting.bullet_width,
                                game_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.color = game_setting.bullet_color
        self.speed = game_setting.bullet_speed

    def update(self):
        self.rect.y -= self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)