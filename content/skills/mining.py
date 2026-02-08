class Mining:
    def __init__(self):
        self.name = "Mining"
        self.level = 1

    def apply(self, character):
        # Skill grants 10% bonus per level to current power
        bonus_mult = 1.0 + (self.level * 0.10)
        character.derived['mining_power'] *= bonus_mult