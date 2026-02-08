from engine.components import BiologicalStructure

class RockNode:
    def __init__(self):
        self.name = "Iron Vein"
        self.hardness = 5 # Reduces damage by 5
        self.body = BiologicalStructure(max_hp=50)