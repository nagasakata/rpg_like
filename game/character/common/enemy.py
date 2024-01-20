from game.character.common.character import Character

import random


class Enemy(Character):
    def __init__(self, 
                 name: str, 
                 hp: int, 
                 mp: int, 
                 attack: int, 
                 difence: int, 
                 magic_attack: int, 
                 magic_difence: int, 
                 speed: int, 
                 skill: dict, 
                 experiment: int,
                 money:int,
                 level_experiment:list,
                 growth_type:list,
                 item:list,
                 image):
        self.experiment = experiment
        self.money = money
        self.item = item
        super().__init__(name, hp, mp, attack, difence, magic_attack, magic_difence, speed, skill, level_experiment, growth_type, image)

    def get_experiment(self):
        return self.experiment

    def get_item(self):
        rate = random.randint(1, 100)
        count, rate_amount = 0, 0
        return_item = None
        for i in self.item:
            if rate <= rate_amount + i[0]:
                return_item = i[1]

            rate_amount = rate_amount + i[0]

        return return_item
