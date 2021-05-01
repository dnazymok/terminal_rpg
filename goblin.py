from enemy import Enemy


class Goblin(Enemy):
    def __init__(self):
        self.name = "Goblin"
        self.health = 40
        self.damage = 7
        self.gold_reward = 10
        self.exp_reward = 10

    def light_attack(self, enemy):
        enemy.health -= self.damage
        print("Гоблин нанес лёгкий удар.")
