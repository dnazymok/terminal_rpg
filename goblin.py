from enemy import Enemy


class Goblin(Enemy):
    name = "Goblin"
    health = 40
    damage = 7
    gold_reward = 10
    exp_reward = 10

    def __init__(self):
        self.health = Goblin.health

