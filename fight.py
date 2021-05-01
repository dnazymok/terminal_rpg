from time import sleep


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
        while True:
            if self.player_turn() == "Win":
                break
            if self.enemy_turn() == "Win":
                break

    def player_turn(self):
        sleep(1)
        self.player.light_attack(self.enemy)
        self.display_fight_status()
        if self.is_enemy_dead():
            print(f"Вы победили!")
            return "Win"

    def enemy_turn(self):
        sleep(1)
        self.enemy.light_attack(self.player)
        self.display_fight_status()
        if self.is_player_dead():
            print(f"{self.enemy.name} победил!")
            return "Win"

    def is_player_dead(self):
        return self.player.health <= 0

    def is_enemy_dead(self):
        return self.enemy.health <= 0
