import random
class ActionResolver:
    @staticmethod
    def mine_target(actor, target):
        print(f"\n> {actor.name} swings pickaxe at {target.name}...")
        
        # 1. Get Data
        power = actor.derived.get('mining_power', 0)
        hardness = target.hardness
        
        # 2. Calculate Damage (Simple Physics)
        # If power < hardness, you might only do 1 damage
        damage = max(1, power - hardness)
        
        # 3. Apply to Target
        remaining_hp = target.body.take_damage(damage)
        
        print(f"  HIT: Dealt {damage} damage against Hardness {hardness}.")
        print(f"  Target HP: {remaining_hp}/{target.body.max_hp}")
        
        if not target.body.is_alive:
            print(f"  SUCCESS: {target.name} shattered!")
            return True # Target destroyed
        return False
    @staticmethod    
    def resolve_combat_round(player, enemy):
        print(f"\n--- COMBAT ROUND: {player.name} vs {enemy.name} ---")
        
        # 1. PLAYER TURN
        p_atk = player.derived['combat_power']
        # Random variance (0.8 to 1.2)
        p_dmg_roll = p_atk * random.uniform(0.8, 1.2)
        p_actual_dmg = max(1, int(p_dmg_roll - enemy.defense))
        
        enemy.body.take_damage(p_actual_dmg)
        print(f"> You slash the {enemy.name} for {p_actual_dmg} damage!")
        
        if not enemy.body.is_alive:
            print(f"  VICTORY: The {enemy.name} collapses.")
            return "victory"

        # 2. ENEMY TURN (If still alive)
        e_atk = enemy.combat_power
        e_dmg_roll = e_atk * random.uniform(0.8, 1.2)
        # Player defense logic would go here (armor etc)
        # For now, base defense is 0
        p_defense = player.derived.get('defense', 0)
        e_actual_dmg = max(1, int(e_dmg_roll - p_defense))
        
        player.body.take_damage(e_actual_dmg)
        print(f"> The {enemy.name} stabs you for {e_actual_dmg} damage!")
        print(f"  Your HP: {int(player.body.current_hp)}/{player.body.max_hp}")

        if not player.body.is_alive:
            print("  DEFEAT: You have died.")
            return "defeat"
            
        return "continue"