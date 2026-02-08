from engine.bases import BaseStat

class Strength(BaseStat):
    # CHANGE: Add 'value=10' as a parameter so we can override it
    def __init__(self, value=10):
        super().__init__("Strength", value=value)

    def apply(self, character):
        # 1 STR = 2 Kinetic Output
        # We check if the attribute exists first to be safe
        if 'kinetic_output' in character.attributes:
            character.attributes['kinetic_output'].value += (self.value * 2.0)