import random, copy

from game.battle.commoon.skill import Skill
from game.character.common.character import Character
from game.item.weapon.weapon_common import Weapon

class Friend(Character):
    def __init__(self, character_type:Character):
        self.character_type = character_type
        self.name = character_type.name
        self.personality = 'tinkering'

        self.hp = character_type.hp
        self.mp = character_type.mp
        self.attack = character_type.attack
        self.difence = character_type.difence
        self.magic_attack = character_type.magic_attack
        self.magic_difence = self.character_type.magic_difence
        self.speed = character_type.speed
        self.skill = character_type.skill
        self.image = character_type.image
        self.level_experiment = character_type.level_experiment
        self.growth_type = character_type.growth_type
        self.experiment = 0
        self.all_experiment = 0
        self.learned_skill = [False, []]
        self.weapon = None

        super().__init__(self.name, 
                         self.hp, 
                         self.mp, 
                         self.attack, 
                         self.difence, 
                         self.magic_attack, 
                         self.magic_difence, 
                         self.speed, 
                         self.skill,
                         self.level_experiment,
                         self.growth_type,
                         self.image)
                         
    def level_up(self):
        if self.level == 100:
            print("you reach to the max level!")
        else:
            self.level = self.level + 1

        for i in self.skill:
            if (i <= self.level) & (not self.skill[i] in self.learned_skill[1]):
                self.learn_skill(self.skill[i])
                self.learned_skill[0] = True
                self.learned_skill[1].append(self.skill[i].get_name())
            else:
                break

        if self.learned_skill[0]:
            int_list = []
            for j in range(self.level):
                int_list.append(j)
            int_list.append(int_list[-1] + 1)

            for k in int_list:
                if k in self.skill:
                    self.skill.pop(k)
                



    def learn_skill(self, skill:Skill):
        self.skill_list[skill.get_name()] = skill

    def add_experiment(self, get:int):
        self.learned_skill = [False, []]
        self.experiment = self.experiment + get
        self.all_experiment = self.all_experiment + get
        up_level = 0
        growth_dict = {'level_bool':False,
                       'level':0,
                       'hp':0,
                       'mp':0,
                       'attack':0,
                       'difence':0,
                       'magic_attack':0,
                       'magic_difence':0,
                       'speed':0}
        while True:
            if self.experiment < self.level_experiment[0]:
                break
            else:
                growth_dict['level_bool'] = True
                self.level_up()
                growth_dict = self.growth(growth_dict)
                self.experiment = self.experiment - self.level_experiment[0]
                self.level_experiment.remove(self.level_experiment[0])
                up_level = up_level + 1
                growth_dict['level'] = up_level
            growth_dict['skill'] = self.learned_skill

        if not self.weapon == None:
            weapon_skill = self.weapon.add_experiment(get)
            if not len(weapon_skill) == 0:
                for skill in weapon_skill:
                    self.learn_skill(skill)
            self.equip_weapon(self.weapon)

        return growth_dict

    def growth(self, growth_dict):
        for i in [0,1,2,3,4,5,6]:
            bonus = random.randint(1, self.growth_type[7])
            if i == 0:
                self.set_hp(self.hp + self.growth_type[i] + bonus)
                if 'hp' in growth_dict:
                 growth_dict['hp'] = growth_dict['hp'] + self.growth_type[i] + bonus
            elif i == 1:
                self.set_mp(self.mp + self.growth_type[i] + bonus)
                growth_dict['mp'] = growth_dict['mp'] + self.growth_type[i] + bonus
            elif i == 2:
                self.set_attack(self.attack + self.growth_type[i] + bonus)
                growth_dict['attack'] = growth_dict['attack'] + self.growth_type[i] + bonus
            elif i == 3:
                self.set_difence(self.difence + self.growth_type[i] + bonus)
                growth_dict['difence'] = growth_dict['difence'] + self.growth_type[i] + bonus
            elif i == 4:
                self.set_magic_attack(self.magic_attack + self.growth_type[i] + bonus)
                growth_dict['magic_attack'] = growth_dict['magic_attack'] + self.growth_type[i] + bonus
            elif i == 5:
                self.set_magic_difence(self.magic_difence + self.growth_type[i] + bonus)
                growth_dict['magic_difence'] = growth_dict['magic_difence'] + self.growth_type[i] + bonus
            else:
                self.set_speed(self.speed + self.growth_type[i] + bonus)
                growth_dict['speed'] = growth_dict['speed'] + self.growth_type[i] + bonus
                
        return growth_dict

    def get_experiment(self):
        return self.experiment

    def get_all_experiment(self):
        return self.all_experiment

    def get_next_experiment(self):
        return self.level_experiment[0] - self.experiment

    def equip_weapon(self, weapon:Weapon):
        self.weapon = weapon
        self.weapon.equip(self.name)
        self.set_hp(self.hp + self.weapon.status[0])
        self.set_mp(self.mp + self.weapon.status[1])
        self.set_attack(self.attack + self.weapon.status[2])
        self.set_difence(self.difence + self.weapon.status[3])
        self.set_magic_attack(self.magic_attack + self.weapon.status[4])
        self.set_magic_difence(self.magic_difence + self.weapon.status[5])
        self.set_speed(self.speed + self.weapon.status[6])


    def release_weapon(self):
        self.set_hp(self.hp - self.weapon.status[0])
        self.set_mp(self.mp - self.weapon.status[1])
        self.set_attack(self.attack - self.weapon.status[2])
        self.set_difence(self.difence - self.weapon.status[3])
        self.set_magic_attack(self.magic_attack - self.weapon.status[4])
        self.set_magic_difence(self.magic_difence - self.weapon.status[5])
        self.set_speed(self.speed - self.weapon.status[6])
        self.weapon.equip(None)
        self.weapon = None
        

