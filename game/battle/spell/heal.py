from game.battle.commoon.spell_common import Spell

class Heal(Spell):
    def __init__(self):
        self.use_mp = 5
        self.power = 10
        self.name = 'Heal'

        super().__init__(self.use_mp, self.power, self.name)