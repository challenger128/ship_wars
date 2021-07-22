import sys
import pygame


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


def keydown_events(event, ship):
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


def check_events(ship):
    """
    Function which processes events
    :param ship: requires for ship movement
    :return: None
    """
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            pygame.quit()
            sys.exit()
        else:
            keyup_events(event, ship)
            keydown_events(event, ship)

def update_screen(game_setting, screen, ship):
    """
    Function which handles screen updates
    :param game_setting: contains important attributes
    :param screen: just our pygame screen
    :param ship: our object which will be drawn
    :return: None
    """
    screen.fill(game_setting.bg_color)
    ship.blit()
    pygame.display.flip()
