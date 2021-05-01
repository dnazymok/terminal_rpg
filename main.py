from prettytable import PrettyTable
from player import Player
from fight import Fight
from goblin import Goblin


class Game:
    def __init__(self):
        self.player = Player()

    def start(self):
        self.print_introduction()
        self.choose_class()
        print("Вы зашли в лес. У вас есть выбор.")
        print("Пойти налево (1)")
        print("Пойти прямо (2)")
        print("Пойти направо (3)")
        choice = input()
        if choice == "1":
            print("Вы встретили Гоблина!")
            print("Завялась драка. К оружию!")
            fight = Fight(self.player, Goblin())
            fight.start()
            print("Вы встретили Гоблина!")
            print("Завялась драка. К оружию!")
            fight = Fight(self.player, Goblin())
            fight.start()

    def print_introduction(self):
        print("Вот такая вот предыстория")

    def choose_class(self):
        print("Выберите класс:")
        character_class = input("Маг, Воин, Убийца?").lower().strip()
        self.player.set_class(character_class)
        self.display_status_bar()

    def display_status_bar(self):
        table = PrettyTable()
        table.field_names = ["Характеристки:", "Уровень"]
        table.add_row([f"Здоровье: {self.player.health}", f"Уровень: {self.player.level}"])
        table.add_row([f"Сила: {self.player.strength}", f"Опыт: {self.player.experience}/100"])
        table.add_row([f"Ловкость: {self.player.agility}", ""])
        table.add_row([f"Интеллект: {self.player.wisdom}", ""])
        table.align = 'r'
        print(table)


g = Game()
g.start()
