class BiologicalStructure:
    def __init__(self, max_hp=100):
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.is_alive = True

    def take_damage(self, amount):
        self.current_hp -= amount
        if self.current_hp <= 0:
            self.current_hp = 0
            self.is_alive = False
        return self.current_hp
    
class Inventory:
    def __init__(self):
        self.bag = [] # List of BaseItem objects
        self.equipment_slots = {
            "main_hand": None,
            "body": None
        }

    def add_item(self, item):
        self.bag.append(item)
        print(f"  [Inventory] Added: {item.name}")

    def equip_item(self, item_name):
        # 1. Find item in bag
        found_item = next((i for i in self.bag if i.name == item_name), None)
        
        if not found_item:
            print(f"  [Error] You don't have '{item_name}'")
            return False

        if not found_item.slot:
            print(f"  [Error] '{item_name}' cannot be equipped.")
            return False

        # 2. Check Slot
        target_slot = found_item.slot
        
        # 3. Swap logic (if something is already there)
        if self.equipment_slots[target_slot] is not None:
            old_item = self.equipment_slots[target_slot]
            self.bag.append(old_item)
            print(f"  [Equip] Unequipped {old_item.name}")

        # 4. Equip
        self.equipment_slots[target_slot] = found_item
        self.bag.remove(found_item)
        print(f"  [Equip] Equipped {found_item.name} to {target_slot}")
        return True

    def get_equipped_bonuses(self):
        """Compiles all stats from all equipped items."""
        total_bonuses = {}
        
        for item in self.equipment_slots.values():
            if item:
                for stat, val in item.bonuses.items():
                    total_bonuses[stat] = total_bonuses.get(stat, 0) + val
                    
        return total_bonuses