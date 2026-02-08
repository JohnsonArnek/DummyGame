class Swordfighting:
    def __init__(self):
        self.name = "Swordfighting"
        self.level = 1

    def apply(self, character):
        # Skill grants +2 Combat Power per level
        bonus = self.level * 2.0
        character.derived['combat_power'] += bonus
        print(f"  [Skill] Swordfighting lvl {self.level} adds +{bonus} Combat Power")