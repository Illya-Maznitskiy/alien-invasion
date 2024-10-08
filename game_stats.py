import json
import os


class GameStats:
    def __init__(self, ai_game):
        """Initialise the game statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        self.high_score = self.get_saved_high_score()

    @staticmethod
    def get_saved_high_score():
        """Gets highest score from file."""
        if os.path.exists("high_score.json"):
            with open("high_score.json") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, dict):
                        return data.get("high_score", 0)
                    elif isinstance(data, int):
                        return data
                except json.JSONDecodeError:
                    print(
                        "Error decoding JSON. "
                        "Returning default high score of 0."
                    )
                    return 0
        print(
            "High score file does not exist. "
            "Returning default high score of 0."
        )
        return 0

    def save_high_score(self):
        """Saves high score to file."""
        with open("high_score.json", "w") as f:
            json.dump({"high_score": self.high_score}, f)

    def reset_stats(self):
        """Initialise the game statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
