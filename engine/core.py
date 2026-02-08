from engine.components import BiologicalStructure
from content.stats.strength import Strength
from content.attributes.kinetic_output import KineticOutput
from content.skills.mining import Mining
# --- ADD THIS LINE BELOW ---
from content.skills.swordfighting import Swordfighting 

class Character:
    def __init__(self, name, gender, race_obj, background_obj):
        self.name = name
        self.gender = gender 
        self.race = race_obj
        self.background = background_obj
        
        # 1. Initialize Base Systems 
        self.stats = {
            "strength": Strength()
        }
        self.attributes = {"kinetic_output": KineticOutput()}
        
        # Now this will work because Swordfighting is imported
        self.skills = {
            "mining": Mining(),
            "swordfighting": Swordfighting() 
        }
        
        self.derived = {
            "mining_power": 0.0,
            "combat_power": 0.0,
            "defense": 0.0
        }

        # 2. APPLY CREATION BONUSES
        self._apply_race_bonuses()
        self._apply_background_bonuses()

    def _apply_race_bonuses(self):
        print(f"Applying Biology: {self.race.name}...")
        for stat_name, bonus in self.race.stat_modifiers.items():
            if stat_name in self.stats:
                self.stats[stat_name].value += bonus

    def _apply_background_bonuses(self):
        print(f"Applying History: {self.background.name}...")
        for skill_name, bonus in self.background.skill_modifiers.items():
            if skill_name in self.skills:
                self.skills[skill_name].level += bonus

    def recalculate(self):
        print(f"\n--- Recalculating {self.name} ---")
        
        # 1. Reset
        for attr in self.attributes.values():
            attr.value = 0
        for key in self.derived:
            self.derived[key] = 0.0

        # 2. Stats -> Attributes & Combat
        for stat in self.stats.values():
            stat.apply(self)
            
            # HARDCODED LOGIC FOR MVP: Strength adds to Combat Power
            if stat.name == "Strength":
                self.derived['combat_power'] += (stat.value * 1.5)

        # 3. Attributes -> Derived
        for attr in self.attributes.values():
            attr.apply(self)
            
        # 4. Skills -> Derived
        for skill in self.skills.values():
            # Mining updates mining_power
            # Swordfighting updates combat_power
            skill.apply(self)

        print(f"Result: Mining Power: {self.derived['mining_power']:.1f}")
        print(f"Result: Combat Power: {self.derived['combat_power']:.1f}")