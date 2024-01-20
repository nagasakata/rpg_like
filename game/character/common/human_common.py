from game.battle.spell import fire
from game.character.common.character import Character

class Human(Character):
    def __init__(self, name:str, status:dict, skill:dict, level_experiment:list, glowth_type:list, image):
        self.work = None
        self.status = status
        self.skill = skill
        self.name = name
        self.level_experiment = level_experiment
        self.growth_type = glowth_type
        self.image = image

        super().__init__(self.name, self.status['hp'], self.status['mp'],
                         self.status['attack'], self.status['difence'],
                         self.status['magic_attack'], self.status['magic_difence'], self.status['speed'],
                         self.skill, self.level_experiment, self.growth_type, self.image)
