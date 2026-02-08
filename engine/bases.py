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