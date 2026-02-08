from engine.creation import CharacterCreator
from engine.resolvers import ActionResolver
from content.entities.rock import RockNode
from content.mobs.goblin import Goblin
from engine.components import BiologicalStructure
from content.skills.swordfighting import Swordfighting

# Helper to pause text
import time

def main():
    # 1. SETUP
    creator = CharacterCreator()
    player = creator.run()
    # Add a body to the player manually for MVP
    player.body = BiologicalStructure(max_hp=50) 
    
    # 2. PHASE 1: MINING
    rock = RockNode()
    print(f"\n[SCENARIO] You see a {rock.name}. You need metal for a weapon.")
    
    while rock.body.is_alive:
        input("(Press Enter to Mine) ")
        ActionResolver.mine_target(player, rock)
        player.recalculate()

    print("\n[EVENT] The rock shatters! You gather the Iron Ore.")
    
    # 3. PHASE 2: CRAFTING (Simulated)
    print("\n[CRAFTING] You hastily forge a Crude Iron Sword.")
    time.sleep(1)
    # Simulate equipping item by boosting stats directly
    player.derived['combat_power'] += 5.0 
    print("  > Equipped: Crude Iron Sword (+5 Combat Power)")
    player.recalculate()

    # 4. PHASE 3: THE AMBUSH
    goblin = Goblin()
    print(f"\n[ALERT] A {goblin.name} heard the noise! It attacks!")
    
    combat_state = "continue"
    while combat_state == "continue":
        cmd = input("\nAction (attack/flee): ").lower()
        
        if cmd == "flee":
            print("You ran away safely... but left your loot behind.")
            break
            
        if cmd == "attack":
            # Run the Resolver
            combat_state = ActionResolver.resolve_combat_round(player, goblin)
            
            # Simulate "Learning by doing"
            if combat_state == "continue":
                player.skills['swordfighting'].level += 1
                print("  (Adrenaline improves your Swordfighting skill!)")
                player.recalculate()

    print("\n=== DEMO COMPLETE ===")

if __name__ == "__main__":
    main()