from engine.components import BiologicalStructure
# In a real version, we would use a loader here. 
# For this MVP, we import content directly to keep it runnable without complex dynamic imports.
from content.stats.strength import Strength
from content.attributes.kinetic_output import KineticOutput
from content.skills.mining import Mining

class Character:
    def __init__(self, name, gender, race_obj, background_obj):
        self.name = name
        self.gender = gender # Purely cosmetic for now
        self.race = race_obj
        self.background = background_obj
        
        # 1. Initialize Base Systems (The Empty Sheets)
        # In a full version, these would load dynamically.
        # For MVP, we manually instantiate the ones we have.
        self.stats = {
            "strength": Strength(), 
            # Add others if you have the files, e.g., Constitution()
        }
        self.attributes = {"kinetic_output": KineticOutput()}
        self.skills = {"mining": Mining()}
        self.derived = {"mining_power": 0.0}

        # 2. APPLY CREATION BONUSES
        self._apply_race_bonuses()
        self._apply_background_bonuses()

    def _apply_race_bonuses(self):
        print(f"Applying Biology: {self.race.name}...")
        for stat_name, bonus in self.race.stat_modifiers.items():
            if stat_name in self.stats:
                self.stats[stat_name].value += bonus
                print(f"  > {stat_name.capitalize()} adjusted by {bonus}")

    def _apply_background_bonuses(self):
        print(f"Applying History: {self.background.name}...")
        for skill_name, bonus in self.background.skill_modifiers.items():
            if skill_name in self.skills:
                self.skills[skill_name].level += bonus
                print(f"  > {skill_name.capitalize()} Skill +{bonus}")

    def recalculate(self):
        """The Loop: Reset -> Apply Stats -> Apply Attributes"""
        print(f"\n--- Recalculating {self.name} ---")
        
        # 1. Reset Attributes & Derived
        for attr in self.attributes.values():
            attr.value = 0
        for key in self.derived:
            self.derived[key] = 0.0

        # 2. Stats -> Attributes
        # (Strength adds to Kinetic Output)
        for stat in self.stats.values():
            stat.apply(self)

        # 3. Attributes -> Derived Mechanics
        # (Kinetic Output adds to Mining Power)
        for attr in self.attributes.values():
            attr.apply(self)
            
        # 4. Skills -> Derived Mechanics
        # (Mining Skill multiplies Mining Power)
        for skill in self.skills.values():
            skill.apply(self)

        print(f"Result: Kinetic Output: {self.attributes['kinetic_output'].value}")
        print(f"Result: Final Mining Power: {self.derived['mining_power']}")