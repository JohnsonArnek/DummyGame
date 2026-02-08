from engine.bases import BaseBackground

class PitSlave(BaseBackground):
    def __init__(self):
        super().__init__("Pit Slave", "You spent your youth breaking rocks in the dark.")
        self.skill_modifiers = {
            "mining": 1 # Starts at Level 1 instead of 0
        }
        self.starting_tags = ["night_vision_poor", "hardened_hands"]