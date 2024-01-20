import pygame

from game.battle.spell import fire
from game.character.about_status.level_experience_type import LevelExperienceType
from game.character.common.human_common import Human

import random, glob

class Mob(Human):
    def __init__(self):
        mob_type = random.randint(0,4)
        if mob_type == 0: # 物理強め　攻撃気味
            hp = random.randint(25, 35)
            mp = random.randint(10, 20)
            attack = random.randint(30, 40)
            difence = random.randint(20, 30)
            magic_attack = random.randint(10, 20)
            magic_difence = random.randint(15, 25)
            speed = random.randint(25, 35)
            growth_hp = random.randint(8, 12)
            growth_mp = random.randint(2, 4)
            growth_attack = random.randint(10, 13)
            growth_difence = random.randint(6, 10)
            growth_magic_attack = random.randint(2, 5)
            growth_magic_difence = random.randint(5, 8)
            growth_speed = random.randint(7, 11)
        elif mob_type == 1: # 物理強め　守備気味
            hp = random.randint(30, 40)
            mp = random.randint(5, 20)
            attack = random.randint(20, 35)
            difence = random.randint(30, 40)
            magic_attack = random.randint(5, 10)
            magic_difence = random.randint(15, 25)
            speed = random.randint(2, 5)
            growth_hp = random.randint(10, 15)
            growth_mp = random.randint(2, 4)
            growth_attack = random.randint(5, 8)
            growth_difence = random.randint(8, 13)
            growth_magic_attack = random.randint(2, 6)
            growth_magic_difence = random.randint(4, 8)
            growth_speed = random.randint(1, 6)
        elif mob_type == 2: # 魔法強め　攻撃気味
            hp = random.randint(15, 25)
            mp = random.randint(30, 40)
            attack = random.randint(5, 9)
            difence = random.randint(6, 13)
            magic_attack = random.randint(25, 35)
            magic_difence = random.randint(20, 30)
            speed = random.randint(10, 25)
            growth_hp = random.randint(5, 15)
            growth_mp = random.randint(10, 20)
            growth_attack = random.randint(2, 6)
            growth_difence = random.randint(4, 6)
            growth_magic_attack = random.randint(8, 13)
            growth_magic_difence = random.randint(6, 10)
            growth_speed = random.randint(5, 15)
        elif mob_type == 3: # 魔法強め　守備気味
            hp = random.randint(25, 35)
            mp = random.randint(20, 30)
            attack = random.randint(2, 6)
            difence = random.randint(12, 17)
            magic_attack = random.randint(20, 30)
            magic_difence = random.randint(30, 40)
            speed = random.randint(3, 7)
            growth_hp = random.randint(10, 16)
            growth_mp = random.randint(7, 17)
            growth_attack = random.randint(2, 10)
            growth_difence = random.randint(5, 11)
            growth_magic_attack = random.randint(5, 10)
            growth_magic_difence = random.randint(6, 14)
            growth_speed = random.randint(2, 7)
        elif mob_type == 4: # 両刀　攻撃気味
            hp = random.randint(15, 25)
            mp = random.randint(20, 30)
            attack = random.randint(22, 32)
            difence = random.randint(8, 13)
            magic_attack = random.randint(22, 32)
            magic_difence = random.randint(8, 13)
            speed = random.randint(5, 20)
            growth_hp = random.randint(5, 15)
            growth_mp = random.randint(5, 15)
            growth_attack = random.randint(5, 10)
            growth_difence = random.randint(3, 8)
            growth_magic_attack = random.randint(5, 10)
            growth_magic_difence = random.randint(3, 8)
            growth_speed = random.randint(5, 10)

        self.status = {'hp':hp,
                       'mp':mp,
                       'attack':attack,
                       'difence':difence, 
                       'magic_attack':magic_attack, 
                       'magic_difence':magic_difence, 
                       'speed':speed}

        self.name = 'None'
        self.skill = {2:fire.Fire()}

        face_file = glob.glob("game/character/common/mob_face/*")
        image_id = random.randint(0, len(face_file)-1)
        self.image = pygame.image.load(face_file[image_id]).convert_alpha()
        self.change_image_size(0.85)
        self.level_experiment = LevelExperienceType().late_20()
        self.growth_type = [growth_hp, growth_mp, growth_attack, growth_difence, growth_magic_attack, growth_magic_difence, growth_speed, 5]

        super().__init__(self.name, self.status, self.skill, self.level_experiment, self.growth_type, self.image)
