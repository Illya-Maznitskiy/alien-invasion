class Settings:
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (7, 0, 36)

        # Alien settings
        self.alien_speed = 1.0

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Alien settings
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 4
        self.bullet_height = 25
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
