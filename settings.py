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
        self.bg_color = (23, 16, 16)
        self.fps = 120
        self.name = 'Ship Wars. Prototype'
        self.ship_speed = 3
        self.bullet_speed = 4
        self.bullet_width = 4
        self.bullet_height = 12
        self.bullet_color = (89, 82, 96)
        self.bullet_allowed = 4
        self.text_color = (254, 152, 152)
