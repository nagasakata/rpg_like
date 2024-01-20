import pygame
from game.character.about_status.level_experience_type import LevelExperienceType

from game.character.common.enemy import Enemy
from game.item.material.material_list import Pileus


class Killermush(Enemy):
    def __init__(self):
        self.image = pygame.image.load("game/character/monster_list/killermush/killermush.png").convert_alpha()
        self.change_image_size(2)
        super().__init__(name='killermush',
                         hp = 13, 
                         mp = 13,
                         attack = 20,
                         difence = 11,
                         magic_attack = 5,
                         magic_difence = 16,
                         speed = 14,
                         skill={},
                         experiment = 10,
                         money = 10,
                         level_experiment = LevelExperienceType().early(),
                         growth_type = [4, 4, 7, 4, 2, 6, 5, 2],
                         item = [(20, Pileus)],
                         image = self.image)