from prettytable import PrettyTable
from player import Player
from fight import Fight
from goblin import Goblin
from chapter_1 import Chapter_1


class Game:
    def __init__(self):
        self.player = Player()

    def start(self):
        chapter_1 = Chapter_1(self.player)
        chapter_1.start()

    def print_introduction(self):
        print("Вот такая вот предыстория")

    def choose_class(self):
        print("Выберите класс:")
        character_class = input("Маг, Воин, Убийца?").lower().strip()
        self.player.set_class(character_class)
        self.display_status_bar()

    def display_status_bar(self):
        table = PrettyTable()
        table.field_names = ["Характеристки:", "Уровень", "Снаряжение"]
        table.add_row([f"Здоровье: {self.player.health}", f"Уровень: {self.player.level}", f"Золото: {self.player.gold}"])
        table.add_row([f"Мана: {self.player.mana}", f"Опыт: {self.player.experience}/100", ""])
        table.add_row([f"Сила: {self.player.strength}", "", ""])
        table.add_row([f"Ловкость: {self.player.agility}", "", ""])
        table.add_row([f"Интеллект: {self.player.wisdom}", "", ""])
        table.add_row([f"Шанс уклониться: {self.player.dodge_chance}", "", ""])
        table.align = 'r'
        print(table)


g = Game()
g.start()
