import pygame
from pygame.sprite import Group
from settings import Setting
from ship import Ship
from stats import GameStats
from manipulation import check_events, update_screen, create_enemies

pygame.init()
game_setting = Setting()
screen = pygame.display.set_mode([game_setting.screen_width,
                                 game_setting.screen_height])
pygame.display.set_caption(game_setting.name)
clock = pygame.time.Clock()
background = pygame.image.load('ship_wars/assets/bg.png').convert_alpha()
ship = Ship(screen, game_setting)
bullets = Group()
enemies = Group()
enemies_bullets = Group()
create_enemies(screen, game_setting, enemies)
stats = GameStats(game_setting)

while True:
    clock.tick(game_setting.fps)
    check_events(screen, game_setting, ship, bullets)
    ship.update()
    bullets.update()
    enemies.update()
    enemies_bullets.update()
    update_screen(screen, background, stats, game_setting, ship, enemies, bullets, enemies_bullets)
