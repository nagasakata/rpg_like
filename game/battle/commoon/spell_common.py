from game.battle.commoon.skill import Skill
from game.character.common.character import Character

class Spell(Skill):
    def __init__(self, use_mp:int, power:int, name:str, target:bool = True):
        self.use_mp = use_mp
        self.power = power
        self.effect = None
        self.element = 'No element'
        self.name = name
        self.target = target # 対称が相手ならTrue

        super().__init__(self.name)


    def use_spell(self, user:Character, target:Character):
        user.mp = user.mp - self.use_mp
        damage = self.power * user.magic_attack - target.magic_difence
        target.set_hp(target.hp - damage)
        print(damage, "damage")
        if target.hp <= 0:
            target.hp = 0
            print(target, "died !")
            return True
        else:
            return False

    def set_element(self, new_element:str):
        self.element = new_element

    def get_element(self):
        return self.element

    def get_use_mp(self):
        return self.use_mp
