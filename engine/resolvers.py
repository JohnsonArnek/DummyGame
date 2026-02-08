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