from enemy import Enemy


class Orc(Enemy):
    name = "Орк"
    health = 100
    damage = 15
    gold_reward = 25
    exp_reward = 25

    def __init__(self):
        self.health = Orc.health

