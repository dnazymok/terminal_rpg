from character_classes.warrior import Warrior
from character_classes.wizard import Wizard
from character_classes.assassin import Assassin
from prettytable import PrettyTable
from random import randint


class Player:
    def __init__(self):
        self.name = None
        self.character_class = None
        self.main_characteristic = None
        self.health = None
        self.strength = None
        self.agility = None
        self.dodge_chance = None
        self.wisdom = None
        self.mana = None
        self.level = 1
        self.experience = 0
        self.gold = 0

    def set_class(self, input_class):
        if input_class == "маг":
            self.set_attributes_to_player_class(Wizard)
        elif input_class == "воин":
            self.set_attributes_to_player_class(Warrior)
        elif input_class == "убийца":
            self.set_attributes_to_player_class(Assassin)

    def set_attributes_to_player_class(self, player_class):
        self.character_class = player_class
        self.health = player_class.health
        self.strength = player_class.strength
        self.agility = player_class.agility
        self.wisdom = player_class.wisdom
        if player_class == Warrior:
            self.main_characteristic = self.strength
        elif player_class == Wizard:
            self.main_characteristic = self.wisdom
        elif player_class == Assassin:
            self.main_characteristic = self.agility
        self.dodge_chance = self.agility * 5
        self.mana = self.wisdom * 10

    def light_attack(self, enemy):
        enemy.health -= self.main_characteristic * 4
        print("Вы нанесли лёгкий удар.")

    def heavy_attack(self, enemy):
        if randint(1, 101) < self.strength * 15:  # chance increases by player strength
            enemy.health -= self.main_characteristic * 8
            print("Вы нанесли тяжёлый удар.")
        else:
            print("Вы попытались нанести тяжёлый удар, но промахнулись")

    def magic_attack(self, enemy):
        enemy.health -= self.wisdom * 10
        print("Вы нанесли магический удар.")
        self.mana -= 3

    def display_status(self):
        table = PrettyTable()
        table.field_names = ["Характеристки:", "Уровень", "Снаряжение"]
        table.add_row([f"Здоровье: {self.health}", f"Уровень: {self.level}", f"Золото: {self.gold}"])
        table.add_row([f"Мана: {self.mana}", f"Опыт: {self.experience}/100", ""])
        table.add_row([f"Сила: {self.strength}", "", ""])
        table.add_row([f"Ловкость: {self.agility}", "", ""])
        table.add_row([f"Интеллект: {self.wisdom}", "", ""])
        table.add_row([f"Шанс уклониться: {self.dodge_chance}", "", ""])
        table.align = 'r'
        print(table)
