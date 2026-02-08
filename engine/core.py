# This file manages the "State" of the application
class GameSession:
    def __init__(self):
        self.player = None
        self.current_location = None
        self.is_running = True

    def start_game(self, player_character):
        self.player = player_character
        print(f"Session started for {self.player.name}")