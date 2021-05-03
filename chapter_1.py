from time import sleep
import os


class Chapter_1:
    def __init__(self, player):
        self.player = player
        self.is_remember_name = False
        self.is_remember_class = False

    def start(self):
        print("Вы проснулись в абсолютной глуши. Ночь, лес, единственный источник света"
              " которвый вы видите это костёр недалеко от вас.")
        print("Пройти к костру: (1)")
        player_choice = input()
        if player_choice.strip() == "1":
            self.campfire()

    def campfire(self):
        self.clear_terminal()
        print("Вы присели возле костра, здесь кажется безопасно.В него ещё почему-то воткнут меч. ")
        if not self.is_remember_name:
            print("Вспомнить как вас зовут: (1)")
        if not self.is_remember_class:
            print("Вспомнить ваше ремесло: (2)")
        if self.is_remember_name and self.is_remember_class:
            print("Забрать меч: (3)")
        player_choice = input().strip()
        if player_choice == "1" and not self.is_remember_name:
            self.is_remember_name = True
            self.remember_name()
        elif player_choice == "2" and not self.is_remember_class:
            self.is_remember_class = True
            self.remember_class()
        elif player_choice == "3":
            self.take_sword_from_campfire()

    def remember_name(self):
        self.clear_terminal()
        print("Кажется вас звали...")
        self.player.name = input()
        self.campfire()

    def remember_class(self):
        self.clear_terminal()
        print("Ваше ремесло: (Маг, Воин, Убийца)")
        self.player.character_class = input()
        self.player.set_class(self.player.character_class.lower())
        self.campfire()

    def take_sword_from_campfire(self):
        self.clear_terminal()
        print("Вы взяли меч. Он в ужасном состоянии, но в случае чего он вас защитит")
        sleep(2)
        print("Больше здесь делать нечего. Вы собрались с силами и решили пойти вглубь леса")

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')