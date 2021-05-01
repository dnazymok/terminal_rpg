from abc import ABC, abstractmethod


class Enemy(ABC):
    @abstractmethod
    def light_attack(self, enemy):
        pass





