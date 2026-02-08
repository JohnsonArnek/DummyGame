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