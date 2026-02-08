from engine.creation import CharacterCreator
from engine.resolvers import ActionResolver
from content.entities.rock import RockNode

def main():
    # 1. RUN CREATION WIZARD
    creator = CharacterCreator()
    player = creator.run()
    
    # 2. INITIALIZE WORLD
    rock = RockNode()
    
    print("\n" + "="*30)
    print(f"Welcome, {player.name} the {player.race.name}.")
    print("You stand before a dense Iron Vein.")
    print("="*30)
    
    # 3. START GAME LOOP
    player.recalculate()
    
    while rock.body.is_alive:
        cmd = input("\nAction (mine/quit): ").lower()
        
        if cmd == "quit":
            break
            
        if cmd == "mine":
            ActionResolver.mine_target(player, rock)
            # Simulate muscle growth
            player.stats['strength'].value += 0.1 
            player.recalculate()

if __name__ == "__main__":
    main()