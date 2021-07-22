import sys
import pygame


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
