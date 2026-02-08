class BaseStat:
    def __init__(self, name, value=10):
        self.name = name
        self.value = value

    def apply(self, character):
        pass

class BaseAttribute:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value

    def apply(self, character):
        pass
    
class BaseRace:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.stat_modifiers = {} # e.g. {'strength': 2}

class BaseBackground:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.skill_modifiers = {} # e.g. {'mining': 1}
        self.starting_tags = []   # e.g. ["literate", "criminal_record"]
        
class BaseItem:
    def __init__(self, name, item_type, stackable=True):
        self.name = name
        self.type = item_type # "resource", "weapon", "armor"
        self.stackable = stackable
        self.quantity = 1
        
        # Equipment Stats
        self.slot = None # "main_hand", "body", etc.
        self.bonuses = {} # e.g. {'strength': 1, 'combat_power': 5}