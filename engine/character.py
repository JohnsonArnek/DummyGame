from engine.components import BiologicalStructure, Inventory
from content.stats.strength import Strength
from content.attributes.kinetic_output import KineticOutput
from content.skills.mining import Mining
from content.skills.swordfighting import Swordfighting

class Character:
    def __init__(self, name, gender, race_obj, background_obj):
        self.name = name
        self.gender = gender 
        self.race = race_obj
        self.background = background_obj
        
        # 1. Initialize Components
        self.inventory = Inventory()
        self.body = BiologicalStructure(max_hp=50) # Moved body init here for consistency
        
        # 2. Initialize Systems
        self.stats = {
            "strength": Strength()
        }
        self.attributes = {"kinetic_output": KineticOutput()}
        self.skills = {
            "mining": Mining(),
            "swordfighting": Swordfighting() 
        }
        
        # 3. Derived Values
        self.derived = {
            "mining_power": 0.0,
            "combat_power": 0.0,
            "defense": 0.0
        }

        # 4. Apply Creation Bonuses
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

        # 2. Base Stats -> Attributes
        for stat in self.stats.values():
            stat.apply(self)
            if stat.name == "Strength":
                self.derived['combat_power'] += (stat.value * 1.5)

        # 3. Equipment -> Stats/Derived
        gear_stats = self.inventory.get_equipped_bonuses()
        for stat_name, value in gear_stats.items():
            if stat_name.lower() in self.stats:
                # Direct stat boost (simplified)
                 if stat_name.lower() == "strength":
                     self.derived['combat_power'] += (value * 1.5)
            elif stat_name in self.derived:
                self.derived[stat_name] += value
                print(f"  [Gear] {stat_name} +{value}")

        # 4. Attributes -> Derived
        for attr in self.attributes.values():
            attr.apply(self)
            
        # 5. Skills -> Derived
        for skill in self.skills.values():
            skill.apply(self)

        print(f"Result: Combat Power: {self.derived['combat_power']:.1f}")