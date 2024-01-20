import pygame
from game.character.about_status.level_experience_type import LevelExperienceType

from game.character.common.enemy import Enemy
from game.item.material.material_list import UndineHair


class Undine(Enemy):
    def __init__(self):
        self.image = pygame.image.load("game/character/monster_list/undine/undine.png").convert_alpha()
        self.change_image_size(2)
        super().__init__(name='undine',
                         hp = 30, 
                         mp = 43,
                         attack = 23,
                         difence = 24,
                         magic_attack = 41,
                         magic_difence = 30,
                         speed = 16,
                         skill={},
                         experiment=10,
                         money = 10,
                         level_experiment = LevelExperienceType().middle(),
                         growth_type = [10, 14, 8, 7, 14, 10, 5, 4],
                         item = [(20, UndineHair)],
                         image = self.image)