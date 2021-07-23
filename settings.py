class Setting:
    """
    Class for storing game settings
    """
    def __init__(self):
        """
        Init game settings, just usual for all
        """
        self.screen_width = 1280
        self.screen_height = 720
        self.fps = 120
        self.name = 'Ship Wars. Prototype'
        self.ship_speed = 4
        self.bullet_speed = 3
        self.bullet_allowed = 5
        self.enemy_speed = 1
        self.enemy_bullet_speed = 3
        self.enemy_bullet_allowed = 8
        self.enemy_direction = 1
