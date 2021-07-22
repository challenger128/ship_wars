import sys
import pygame
from bullet import Bullet

def keyup_events(event, ship):
    """
    Takes an event and check if it is an keyup-event.
    If it is the keyup-event, ship movement will be stopped
    :param event: Takes an event from queue
    :param ship: Takes our ship
    :return: None
    """
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False


def keydown_events(screen, game_setting, event, ship, bullets):
    """
    Takes an event and check if it is an keydown-event.
    If it is the keyup-event, ship movement will be started
    :param event: Takes an event from queue
    :param ship: Takes our ship
    :return: None
    """
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        if event.key == pygame.K_LEFT:
            ship.moving_left = True
        if event.key == pygame.K_SPACE:
            new_bullet = Bullet(screen, game_setting, ship)
            bullets.add(new_bullet)

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

def update_screen(screen, game_setting, ship, bullets):
    """
    Function which handles screen updates
    :param screen: just our pygame screen
    :param game_setting: contains important attributes
    :param ship: our object which will be drawn
    :param bullets: our group of bullet which we will draw
    :return: None
    """
    screen.fill(game_setting.bg_color)
    ship.blit()
    for bullet in bullets:
        bullet.draw()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    pygame.display.flip()
