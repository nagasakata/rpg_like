from game.battle.commoon.spell_common import Spell

class Thunder(Spell):
    def __init__(self):
        self.use_mp = 5
        self.power = 10
        self.name = 'Thunder'

        super().__init__(self.use_mp, self.power, self.name)