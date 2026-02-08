from engine.components import BiologicalStructure
from content.stats.strength import Strength

class Goblin:
    def __init__(self):
        self.name = "Scavenger Goblin"
        
        # 1. Body
        self.body = BiologicalStructure(max_hp=30)
        
        # 2. Stats (Simple version for mobs)
        self.stats = {
            "strength": Strength(value=5) # Weaker than a human
        }
        
        # 3. Derived Combat Stats (Hardcoded for MVP simplicity)
        # In full engine, mobs would run .recalculate() too.
        self.combat_power = 8.0  # Base damage
        self.defense = 2.0       # Natural skin toughness