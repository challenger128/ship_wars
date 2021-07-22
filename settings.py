class Setting:
    """
    Class for storing game settings
    """
    def __init__(self):
        """
        Init game settings, just usual for all
        """
        self.screen_width = 1270
        self.screen_height = 720
        self.bg_color = (225, 229, 234)
        self.fps = 120
        self.name = 'Ship Wars. Prototype'
        self.ship_speed = 3
        self.bullet_speed = 4
        self.bullet_width = 4
        self.bullet_height = 12
        self.bullet_color = (89, 82, 96)
