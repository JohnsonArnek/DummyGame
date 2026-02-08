from engine.bases import BaseRace

class Dwarf(BaseRace):
    def __init__(self):
        super().__init__("Dwarf", "Stocky, dense, and adapted to the deep.")
        # Dwarves start with higher base Strength and Constitution
        self.stat_modifiers = {
            "strength": 3,
        }