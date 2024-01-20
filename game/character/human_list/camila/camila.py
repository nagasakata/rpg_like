import pygame

from game.battle.spell import fire
from game.character.about_status.level_experience_type import LevelExperienceType
from game.character.common.human_common import Human

class Camila(Human):
    def __init__(self):
        self.status = {'hp':36,
                       'mp':25,
                       'attack':24,
                       'difence':23, 
                       'magic_attack':17, 
                       'magic_difence':15, 
                       'speed':18}

        self.name = 'Camila'
        self.skill = {2:fire.Fire()}
        self.image = pygame.image.load("game/character/human_list/camila/camila_face.png").convert_alpha()
        self.change_image_size(0.85)
        self.level_experiment = LevelExperienceType().late_20()
        self.growth_type = [12, 3, 11, 8, 9, 4, 6, 5]

        super().__init__(self.name, self.status, self.skill, self.level_experiment, self.growth_type, self.image)
