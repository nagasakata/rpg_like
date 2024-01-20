from game.battle.commoon.spell_common import Spell

class Freeze(Spell):
    def __init__(self):
        self.use_mp = 5
        self.power = 10
        self.name = 'Freeze'

        super().__init__(self.use_mp, self.power, self.name)