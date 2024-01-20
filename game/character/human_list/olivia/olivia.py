import pygame

from game.battle.spell import fire
from game.character.about_status.level_experience_type import LevelExperienceType
from game.character.common.human_common import Human

class Olivia(Human):
    def __init__(self):
        self.status = {'hp':10000,
                       'mp':15000,
                       'attack':500,
                       'difence':1000, 
                       'magic_attack':500, 
                       'magic_difence':1000, 
                       'speed':1000}

        self.name = 'Olivia'
        self.skill = {5:fire.Fire()}
        self.image = pygame.image.load("game/character/human_list/olivia/olivia_face.png").convert_alpha()
        self.change_image_size(0.85)
        self.level_experiment = LevelExperienceType().late_20()

        super().__init__(self.name, self.status, self.skill, self.level_experiment, self.image)
