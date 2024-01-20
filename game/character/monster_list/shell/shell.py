import pygame
from game.character.about_status.level_experience_type import LevelExperienceType

from game.character.common.enemy import Enemy
from game.item.material.material_list import ClamShell


class Shell(Enemy):
    def __init__(self):
        self.image = pygame.image.load("game/character/monster_list/shell/shell.png").convert_alpha()
        self.change_image_size(2)
        super().__init__(name='shell',
                         hp = 25, 
                         mp = 10,
                         attack = 18,
                         difence = 25,
                         magic_attack = 5,
                         magic_difence = 4,
                         speed = 5,
                         skill={},
                         experiment=10,
                         money = 10,
                         level_experiment = LevelExperienceType().early(),
                         growth_type = [8, 3, 7, 6, 2, 1, 3, 2],
                         item = [(20, ClamShell)],
                         image = self.image)