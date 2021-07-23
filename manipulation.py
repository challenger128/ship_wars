import sys
import pygame
from bullet import Bullet
from enemy import EnemyShip


def create_enemies(screen, game_setting, enemies):
    enemy = EnemyShip(screen, game_setting)
    space = game_setting.screen_width - enemy.rect.width
    number_enemies = space // (2 * enemy.rect.width)
    for number in range(number_enemies):
        enemy = EnemyShip(screen, game_setting)
        enemy.rect.x = enemy.rect.width + 2 * number * enemy.rect.width
        enemies.add(enemy)


def create_ship_bullet(screen, game_setting, ship, bullets):
    """
    Function which creates new bullet in Group of Sprites
    :param screen: required for Bullet constructor
    :param game_setting: required for Bullet constructor, its attribute
    limits amount of bullets
    :param ship: required for Bullet constructor
    :param bullets: required for Bullet constructor
    :return: None
    """
    if len(bullets) < game_setting.bullet_allowed:
        new_bullet = Bullet(screen, game_setting, ship)
        bullets.add(new_bullet)


def mousedown_events(screen, game_setting, event, ship, bullets):
    """
    Takes an event and check if it is an mouse-button-down event.
    If it is the mouse-button-down, ship will fire
    :param screen: required for creating bullet
    :param game_setting: required for creating bullet
    :param event: event object which we will check
    :param ship: required for creating bullet
    :param bullets: required for creating bullet
    :return: None
    """
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            create_ship_bullet(screen, game_setting, ship, bullets)


def keyup_events(event, ship):
    """
    Takes an event and check if it is an keyup-event.
    If it is the keyup-event, ship movement will be stopped
    :param event: Takes an event from queue
    :param ship: Takes our ship
    :return: None
    """
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            ship.moving_right = False
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            ship.moving_left = False


def keydown_events(screen, game_setting, event, ship, bullets):
    """
    Takes an event and check if it is an keydown-event.
    If it is the keydown-event, ship movement will start moving or shooting
    :param screen: required for creating bullet
    :param game_setting: required for creating bullet
    :param event: event object which we will check
    :param ship: required for creating bullet, changes attribute which respond for moving
    :param bullets: required for creating bullet
    :return: None
    """
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            ship.moving_right = True
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            ship.moving_left = True
        if event.key == pygame.K_SPACE:
            create_ship_bullet(screen, game_setting, ship, bullets)


def check_events(screen, game_setting, ship, bullets):
    """
    Function which processes events
    :param screen: requires for keydown_events call
    :param game_setting: requires for keydown_events call
    :param ship: control movement of ship
    :param bullets: create bullets in keydown_events call
    :return: None
    """
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            pygame.quit()
            sys.exit()
        else:
            keyup_events(event, ship)
            keydown_events(screen, game_setting, event, ship, bullets)
            mousedown_events(screen, game_setting, event, ship, bullets)

def update_screen(screen, background, game_setting, ship, enemies, bullets):
    """
    Function which handles screen updates
    :param screen: just our pygame screen
    :param ship: our object which will be drawn
    :param bullets: our group of bullet which we will draw
    :return: None
    """
    screen.blit(background, (0, 0))
    ship.blit()
    enemies.draw(screen)
    for bullet in bullets:
        bullet.blit()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    pygame.display.flip()
