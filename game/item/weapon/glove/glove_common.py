from game.battle.spell.thunder import Thunder
from game.item.weapon.weapon_common import Weapon


class GomGlove(Weapon):
    def __init__(self):
        self.name = 'gom glove'
        self.money = 10
        self.skill = {1:Thunder(),
                      2:None,
                      3:None,
                      4:None,
                      5:None,
                      6:None,
                      7:None,
                      8:None,
                      9:None,
                      10:None}
        self.growth = [0, 0, 3, 1, 0, 0, 3]
        self.status = [0, 0, 5, 0, 0, 0, 5]
        self.level_delimiter = {1:10, 
                                2:20,
                                3:30,
                                4:40,
                                5:50,
                                6:60,
                                7:70,
                                8:80,
                                9:90,
                                10:100}

        super().__init__(self.name, self.money, self.skill, self.status, self.growth, self.level_delimiter)