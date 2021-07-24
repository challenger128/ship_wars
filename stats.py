class GameStats():

    def __init__(self, game_setting):
        self.game_setting = game_setting
        self.reset_stats()

    def reset_stats(self):
        self.ship_health = self.game_setting.ship_health
