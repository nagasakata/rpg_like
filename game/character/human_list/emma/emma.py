import pygame

from game.battle.spell import fire, freeze, heal, motivate, thunder, wind
from game.character.about_status.level_experience_type import LevelExperienceType
from game.character.common.human_common import Human

class Emma(Human):
    def __init__(self):
        self.status = {'hp':20,
                       'mp':35,
                       'attack':13,
                       'difence':19, 
                       'magic_attack':28, 
                       'magic_difence':35, 
                       'speed':13}

        self.name = 'Emma'
        self.skill = {2:fire.Fire(),
                      3:wind.Wind(),
                      4:heal.Heal(),
                      5:freeze.Freeze(),
                      6:thunder.Thunder(),
                      7:motivate.Motivate()}
        self.image = pygame.image.load("game/character/human_list/emma/emma_face.png").convert_alpha()
        self.change_image_size(0.85)
        self.level_experiment = LevelExperienceType().late_20()
        self.growth_type = [7, 8, 5, 7, 15, 14, 4, 5]

        super().__init__(self.name, self.status, self.skill, self.level_experiment, self.growth_type, self.image)
