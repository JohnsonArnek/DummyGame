from content.races.dwarf import Dwarf
from content.races.human import Human
from content.backgrounds.pit_slave import PitSlave
from engine.character import Character

class CharacterCreator:
    def run(self):
        print("\n=== SOUL FORGING (Character Creation) ===")
        
        # 1. Name
        name = input("Enter your Name: ") or "Drifter"
        
        # 2. Gender
        gender = input("Enter Gender (M/F/Nb): ")
        
        # 3. Race Selection
        print("\n--- Select Form ---")
        races = [Human(), Dwarf()]
        for i, r in enumerate(races):
            print(f"{i+1}. {r.name}: {r.description} {r.stat_modifiers}")
            
        choice = int(input("Choose Race (Number): ") or 1) - 1
        selected_race = races[choice]
        
        # 4. Background Selection
        print("\n--- Select Origin ---")
        # In MVP we only have one, but list allows expansion
        backgrounds = [PitSlave()] 
        for i, b in enumerate(backgrounds):
            print(f"{i+1}. {b.name}: {b.description} {b.skill_modifiers}")
            
        choice = int(input("Choose Background (Number): ") or 1) - 1
        selected_bg = backgrounds[choice]

        # 5. Appearance (Placeholder)
        print("\n--- Appearance ---")
        print("[!] Visual Cortex Module not loaded. Using default avatar.")
        print("...Skipping detailed sliders...")
        
        # 6. Finalize
        print(f"\n[System] Constructing {selected_race.name} {selected_bg.name}...")
        return Character(name, gender, selected_race, selected_bg)