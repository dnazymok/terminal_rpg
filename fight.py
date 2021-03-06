from time import sleep
from random import randint


class Fight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def display_fight_status(self):
        print(
            f"----- Вы: {self.player.health}, "
            f"{self.enemy.name}: {self.enemy.health} -----", "\n")

    def start(self):
        """Game loop. Breaks if player or enemy turn ends in victory"""
        self.display_fight_status()
        while True:
            if self.player_turn() == "Win":
                self.player.gold += self.enemy.gold_reward
                self.player.experience += self.enemy.exp_reward
                break
            if self.enemy_turn() == "Win":
                print("На этом ваше приключение закончилось.")
                print("YOU DIED")
                break

    def player_turn(self):
        sleep(1)
        print("Лёгкая атака (гарантированое попадание, средний урон): (1)")
        print("Тяжёлая атака (чем больше силы тем больше шанс попадания, большой урон): (2)")
        print("Магическая атака (урон зависит от мудрости персонажа, отнимает ману): (3)")
        while True:
            choice = input()
            if choice == "1":
                self.player.light_attack(self.enemy)
                break
            elif choice == "2":
                self.player.heavy_attack(self.enemy)
                break
            elif choice == "3":
                self.player.magic_attack(self.enemy)
                break
            else:
                print("Выберете вариант из предложеных")
        self.display_fight_status()
        if self.is_enemy_dead():
            return "Win"

    def enemy_turn(self):
        sleep(1)
        if randint(1, 101) <= self.player.dodge_chance:
            print("Вы уклонились от удара!")
        else:
            self.enemy.light_attack(self.player)
        self.display_fight_status()
        if self.is_player_dead():
            print(f"{self.enemy.name} победил!")
            return "Win"

    def is_player_dead(self):
        return self.player.health <= 0

    def is_enemy_dead(self):
        return self.enemy.health <= 0

