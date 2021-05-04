from time import sleep
from fight import Fight
from goblin import Goblin

import os


class Chapter_1:
    def __init__(self, player):
        self.player = player
        self.is_remember_name = False
        self.is_remember_class = False
        self.is_goblin_dead = False

    def start(self):
        self.update_terminal_view()
        print("Вы проснулись в абсолютной глуши. Ночь, лес, единственный источник света"
              " которвый вы видите это костёр недалеко от вас.")
        print("Пройти к костру: (1)")
        while True:
            player_choice = input()
            if player_choice.strip() == "1":
                self.campfire()
                break
            else:
                print("Выберете вариант из предложеных")

    def campfire(self):
        while True:
            self.update_terminal_view()
            print("Вы присели возле костра, здесь кажется безопасно.В него ещё почему-то воткнут меч. ")
            if not self.is_remember_name:
                print("Вспомнить как вас зовут: (1)")
            if not self.is_remember_class:
                print("Вспомнить ваше ремесло: (2)")
            if self.is_remember_name and self.is_remember_class:
                print("Забрать меч: (3)")
            player_choice = input().strip()
            if player_choice == "1" and not self.is_remember_name:
                self.remember_name()
                self.is_remember_name = True
            elif player_choice == "2" and not self.is_remember_class:
                self.remember_class()
                self.is_remember_class = True
            elif player_choice == "3":
                self.take_sword_from_campfire()
                break
            else:
                print("Выберете вариант из предложеных")

    def remember_name(self):
        self.update_terminal_view()
        print("Кажется вас звали...")
        self.player.name = input()

    def remember_class(self):
        self.update_terminal_view()
        print("Кажется вы были:")
        print("Воином: (1)")
        print("Магом (2)")
        print("Убийцей (3)")
        while True:
            choice = input().lower()
            if choice == "1":
                self.player.character_class = "воин"
                self.player.set_class("воин")
                break
            elif choice == "2":
                self.player.character_class = "маг"
                self.player.set_class("маг")
                break
            elif choice == "3":
                self.player.character_class = "убийца"
                self.player.set_class("убийца")
                break
            else:
                print("Выберете вариант из предложеных")
                sleep(1)

    def take_sword_from_campfire(self):
        self.update_terminal_view()
        print("Вы взяли меч. Он в ужасном состоянии, но в случае чего он вас защитит")
        sleep(2)
        print("Больше здесь делать нечего. Вы собрались с силами и решили пойти вглубь леса")
        self.go_in_wood()

    def go_in_wood(self):
        count = 0
        while True:
            self.update_terminal_view()
            count += 1
            if count == 1:
                print(
                    "Вы шли с осторожностью по тропинке, в любой момент ожидая опасности. Но к счастью ничего страшного не "
                    "произошло, вы дошли до развилки. На тропинке слева виднеются следы, кажется человеческие. "
                    "Нужно решить куда свернуть")
            else:
                print("Вы вернулись на развилку")
            if not self.is_goblin_dead:
                print("Свернуть налево: (1)")
            print("Свернуть направо: (2)")
            choice = input()
            if choice == "1" and not self.is_goblin_dead:
                self.player_go_left()
            elif choice == "2":
                self.player_go_right()
            else:
                print("Выберете вариант из предложеных")

    def player_go_left(self):
        self.update_terminal_view()
        print("Вы идете по следам и замечаете что они ведут вас к трупу человека в доспехах. Осторожно осмотревшись "
              "вы замечаете гоблина. У вас ещё есть время вернуться назад пока он вас не заметил.")
        print("Напасть на гоблина: (1)")
        print("Убежать: (2)")
        while True:
            choice = input()
            if choice == "1":
                self.update_terminal_view()
                print("Вы решились напасть первым")
                fight = Fight(self.player, Goblin())
                fight.start()
                print("У гоблина вы нашли несколько монет в кошельке. Так же вы видите, что тропинка заканчивается, "
                      "нужно возвращаться обратно")
                self.is_goblin_dead = True
                print("Вернуться к развилке: (1)")
                while True:
                    choice = input()
                    if choice == "1":
                        break
                    else:
                        print("Выберете вариант из предложеных")
                break
            elif choice == "2":
                break
            else:
                print("Выберете вариант из предложеных")

    def player_go_right(self):
        pass

    def update_terminal_view(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.is_remember_class:
            self.player.display_status()