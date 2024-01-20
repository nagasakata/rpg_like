import pygame

from game.battle.spell import fire
from game.character.about_status.level_experience_type import LevelExperienceType
from game.character.common.human_common import Human

class Riley(Human):
    def __init__(self):
        self.status = {'hp':20000,
                       'mp':1000,
                       'attack':2000,
                       'difence':1500, 
                       'magic_attack':100, 
                       'magic_difence':200, 
                       'speed':1500}

        self.name = 'Riley'
        self.skill = {5:fire.Fire()}
        self.image = pygame.image.load("game/character/human_list/riley/riley_face.png").convert_alpha()
        self.change_image_size(0.85)
        self.level_experiment = LevelExperienceType().late_20()

        super().__init__(self.name, self.status, self.skill, self.level_experiment, self.image)
