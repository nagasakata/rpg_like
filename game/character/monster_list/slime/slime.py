import pygame
from game.character.about_status.level_experience_type import LevelExperienceType

from game.character.common.enemy import Enemy
from game.item.material.material_list import SlimeJelly


class Slime(Enemy):
    def __init__(self):
        self.image = pygame.image.load("game/character/monster_list/slime/slime.png").convert_alpha()
        self.change_image_size(2)
        super().__init__(name='slime',
                         hp = 20, 
                         mp = 15,
                         attack = 15,
                         difence = 13,
                         magic_attack = 7,
                         magic_difence = 5,
                         speed = 11,
                         skill={},
                         experiment = 500,
                         money = 10,
                         level_experiment = LevelExperienceType().early(),
                         growth_type = [6, 4, 8, 8, 3, 3, 3, 2],
                         item = [(20, SlimeJelly)],
                         image = self.image)