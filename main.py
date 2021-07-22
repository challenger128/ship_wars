import pygame
from settings import Setting

# Init game engine
pygame.init()
game_setting = Setting()
screen = pygame.display.set_mode([game_setting.screen_width,
                                 game_setting.screen_height])
pygame.display.set_caption(game_setting.name)

# Loop until the user clicks the close button.
running = True
clock = pygame.time.Clock()


while running:

    # Set the framerate
    clock.tick(game_setting.fps)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            running = False

    # Clear the screen and set the screen background
    screen.fill(game_setting.bg_color)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
