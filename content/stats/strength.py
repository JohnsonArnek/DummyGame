from engine.bases import BaseStat

class Strength(BaseStat):
    def __init__(self):
        super().__init__("Strength", value=10) # Base 10

    def apply(self, character):
        # 1 STR = 2 Kinetic Output
        character.attributes['kinetic_output'].value += (self.value * 2.0)