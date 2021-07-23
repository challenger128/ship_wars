import pygame
from pygame.sprite import Group
from settings import Setting
from ship import Ship
from manipulation import check_events, update_screen

pygame.init()
game_setting = Setting()
screen = pygame.display.set_mode([game_setting.screen_width,
                                 game_setting.screen_height])
pygame.display.set_caption(game_setting.name)
pygame.display.set_icon(pygame.image.load('ship_wars/assets/ship.png'))
clock = pygame.time.Clock()
ship = Ship(screen, game_setting)
bullets = Group()

while True:
    clock.tick(game_setting.fps)
    check_events(screen, game_setting, ship, bullets)
    ship.update()
    bullets.update()
    update_screen(screen, game_setting, ship, bullets)
