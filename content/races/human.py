from engine.bases import BaseRace

class Human(BaseRace):
    def __init__(self):
        super().__init__("Human", "Adaptable and ambitious.")
        # Humans are average
        self.stat_modifiers = {
            "strength": 1
        }