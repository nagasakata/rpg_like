import pygame
from game.character.common.enemy_member import EnemyMember

from game.object.field_object.field_common import FieldCommon
from game.character.monster_list import *

import random, copy

class EncountObject():
    def __init__(self):
        self.glass = EncountGlass()
        self.swamp = EncountSwamp()

    def get_encount_object_color(self):
        object_color_list = []
        object_color_list.append(self.glass.color)
        object_color_list.append(self.swamp.color)

        return object_color_list

    def color_field(self, now_color:pygame.Color):
        now_field = None

        if now_color == self.glass.color:
            now_field = self.glass
        elif now_color == self.swamp.color:
            now_field = self.swamp
        
        return now_field

class EncountGlass(FieldCommon):
    def __init__(self):
        self.color = pygame.Color(0, 101, 0)
        self.enemy_list = [slime.Slime(), 
                           killermush.Killermush()]
        self.enemy_member = set_enemy(self.enemy_list, 1, 3)

        super().__init__(self.color)

class EncountSwamp(FieldCommon):
    def __init__(self):
        self.color = pygame.Color(153, 255, 204)
        self.enemy_list = [shell.Shell(), 
                           fish.Fish(),
                           undine.Undine()]
        self.enemy_member = set_enemy(self.enemy_list, 4, 5)

        super().__init__(self.color)

def set_enemy(enemy_list, min_num, max_num):
    enemies = EnemyMember()
    enemy_many = random.randint(min_num, max_num)
    for i in range(enemy_many):
        j = random.randint(0, len(enemy_list)-1)
        enemies.add_enemy(copy.copy(enemy_list[j]))

    return enemies

