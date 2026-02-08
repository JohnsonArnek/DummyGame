from engine.creation import CharacterCreator
from engine.resolvers import ActionResolver
from content.entities.rock import RockNode
from content.mobs.goblin import Goblin
from content.items.iron_ore import IronOre
from content.items.iron_sword import IronSword
# We no longer need to import BiologicalStructure here!

def main():
    # 1. SETUP
    creator = CharacterCreator()
    player = creator.run()
    
    # REMOVED: player.body = BiologicalStructure(max_hp=50) 
    # (The Character class now does this automatically)
    
    # 2. MINING PHASE
    rock = RockNode()
    print(f"\n[SCENARIO] You see a {rock.name}.")
    
    # Initial calculation to set up stats
    player.recalculate()
    
    while rock.body.is_alive:
        input("(Press Enter to Mine) ")
        # We check if mining was successful (returns True/False)
        if ActionResolver.mine_target(player, rock):
            # REAL INVENTORY LOGIC
            ore = IronOre()
            print(f"*** You picked up: {ore.name} ***")
            player.inventory.add_item(ore)
            break
    
    # 3. CRAFTING PHASE
    print("\n[CRAFTING] You head to the forge...")
    
    # Check if we have the ore
    has_ore = any(i.name == "Iron Ore" for i in player.inventory.bag)
    
    if has_ore:
        # Remove Ore
        ore_item = next(i for i in player.inventory.bag if i.name == "Iron Ore")
        player.inventory.bag.remove(ore_item)
        print(f"  > Smelted {ore_item.name}...")
        
        # Create Sword
        sword = IronSword()
        player.inventory.add_item(sword)
        
        # Equip it
        player.inventory.equip_item("Iron Sword")
        
        # Recalculate to see the stats change
        player.recalculate()
    else:
        print("You don't have the ore required!")

    # 4. COMBAT PHASE
    goblin = Goblin()
    print(f"\n[ALERT] A {goblin.name} attacks!")
    
    combat_state = "continue"
    while combat_state == "continue":
        cmd = input("\nAction (attack/flee): ").lower()
        
        if cmd == "flee":
            print("You ran away!")
            break
            
        if cmd == "attack":
            combat_state = ActionResolver.resolve_combat_round(player, goblin)

    print("\n=== DEMO COMPLETE ===")

if __name__ == "__main__":
    main()