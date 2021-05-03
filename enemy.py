from abc import ABC, abstractmethod


class Enemy(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def health(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @property
    @abstractmethod
    def gold_reward(self):
        pass

    @property
    @abstractmethod
    def exp_reward(self):
        pass

    def light_attack(self, enemy):
        enemy.health -= self.damage
        print(f"{self.name} нанес лёгкий удар.")





