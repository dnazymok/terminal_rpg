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


g = Game()
g.start()
