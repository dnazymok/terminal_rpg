from character_classes.warrior import Warrior
from character_classes.wizard import Wizard
from character_classes.assassin import Assassin
from prettytable import PrettyTable


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
            self.character_class = Wizard
            self.health = Wizard.health
            self.strength = Wizard.strength
            self.agility = Wizard.agility
            self.wisdom = Wizard.wisdom
            self.main_characteristic = self.wisdom
            self.dodge_chance = self.agility * 5
            self.mana = self.wisdom * 10
        elif input_class == "воин":
            self.character_class = Warrior
            self.health = Warrior.health
            self.strength = Warrior.strength
            self.agility = Warrior.agility
            self.wisdom = Warrior.wisdom
            self.main_characteristic = self.strength
            self.dodge_chance = self.agility * 5
            self.mana = self.wisdom * 10
        elif input_class == "убийца":
            self.character_class = Assassin
            self.health = Assassin.health
            self.strength = Assassin.strength
            self.agility = Assassin.agility
            self.wisdom = Assassin.wisdom
            self.main_characteristic = self.agility
            self.dodge_chance = self.agility * 5
            self.mana = self.wisdom * 10

    def light_attack(self, enemy):
        enemy.health -= self.main_characteristic * 4
        print("Вы нанесли лёгкий удар.")

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
