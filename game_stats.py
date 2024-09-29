import json
import os


class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        self.high_score = self.get_saved_high_score()

    @staticmethod
    def get_saved_high_score():
        if os.path.exists("high_score.json"):
            with open("high_score.json") as f:
                try:
                    # Try loading as a dictionary
                    data = json.load(f)
                    if isinstance(data, dict):
                        return data.get("high_score", 0)
                    # If it's just an integer
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
        with open("high_score.json", "w") as f:
            json.dump({"high_score": self.high_score}, f)

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
