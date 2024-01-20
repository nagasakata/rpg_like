import pygame
from game.character.about_status.level_experience_type import LevelExperienceType

from game.character.common.enemy import Enemy
from game.item.material.material_list import FishBone


class Fish(Enemy):
    def __init__(self):
        self.image = pygame.image.load("game/character/monster_list/fish/fish.png").convert_alpha()
        self.change_image_size(2)
        super().__init__(name='fish',
                         hp = 8, 
                         mp = 27,
                         attack = 10,
                         difence = 9,
                         magic_attack = 22,
                         magic_difence = 15,
                         speed = 16,
                         skill={},
                         experiment=5,
                         money = 10,
                         level_experiment = LevelExperienceType().early(),
                         growth_type = [2, 8, 3, 3, 7, 4, 5, 3],
                         item = [(20, FishBone)],
                         image = self.image)