import copy

from game.character.common.character import Character
from game.character.common.enemy import Enemy

class EnemyMember():
    def __init__(self):
        self.enemies = dict()

    def add_enemy(self, enemy:Enemy):
        if not (1 in self.enemies):
            self.enemies[1] = enemy
        else:
            for i in self.enemies:
                if not i+1 in self.enemies:
                    self.enemies[i+1] = enemy
                    break


    def kill_enemy(self, enemy:Enemy):
        for i in self.enemies:
            if self.enemies[i] == enemy:
                self.enemies.pop(i)
                break

        pre_enemies = dict()
        count = 1
        for j in self.enemies:
            pre_enemies[count] = self.enemies[j]
            count = count + 1

        self.enemies = pre_enemies


    def is_delited(self):
        return not (len(self.enemies) == 0)