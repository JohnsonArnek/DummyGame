from engine.bases import BaseAttribute

class KineticOutput(BaseAttribute):
    def __init__(self):
        super().__init__("Kinetic Output")

    def apply(self, character):
        # Kinetic Output directly increases Mining Power
        character.derived['mining_power'] += self.value