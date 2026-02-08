from engine.bases import BaseItem

class IronSword(BaseItem):
    def __init__(self):
        super().__init__("Iron Sword", "weapon")
        self.slot = "main_hand"
        # This maps directly to character.derived keys
        self.bonuses = {
            "combat_power": 5.0
        }