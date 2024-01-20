import copy
import pygame

class Character():
    def __init__(self, 
                 name:str,
                 hp:int, 
                 mp:int, 
                 attack:int, 
                 difence:int, 
                 magic_attack:int, 
                 magic_difence:int, 
                 speed:int,
                 skill:dict,
                 level_experiment:list,
                 growth_type:list,
                 image:pygame.image):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.difence = difence
        self.magic_attack = magic_attack
        self.magic_difence = magic_difence
        self.speed = speed
        self.level = 1
        self.own_element = "Normal"
        self.skill_list = dict()
        self.skill = skill
        self.image = image
        self.level_experiment = level_experiment
        self.growth_type = growth_type
        self.image_rect = self.image.get_rect()
        self.original_image_size = copy.copy(self.image.get_size())

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_attack(self):
        return self.attack

    def get_difence(self):
        return self.difence

    def get_magic_attack(self):
        return self.magic_attack

    def get_magic_difence(self):
        return self.magic_difence

    def get_speed(self):
        return self.speed

    def set_hp(self, new_hp:int):
        self.hp = new_hp

    def set_mp(self, new_mp:int):
        self.mp = new_mp

    def set_attack(self, new_attack:int):
        self.attack = new_attack

    def set_difence(self, new_difence:int):
        self.difence = new_difence

    def set_magic_attack(self, new_magic_attack:int):
        self.magic_attack = new_magic_attack

    def set_magic_difence(self, new_magic_difence:int):
        self.magic_difence = new_magic_difence

    def set_speed(self, new_speed:int):
        self.speed = new_speed

    def set_name(self, new_name:str):
        self.name = new_name


    def set_level(self, new_level:int):
        if (new_level <= 100) & (new_level >= 1):
            self.level = new_level
        else:
            print("level must be 1 ~ 100")

        for i in self.skill:
            if i <= new_level:
                self.skill_list[self.skill[i].get_name()] = self.skill[i]
            else:
                break

    def set_element(self, new_own_element:str):
        self.own_element = new_own_element

    def get_element(self):
        return self.own_element

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_image(self):
        return self.image

    def draw_image(self, screen, center_x, center_y):
        self.image_rect.center = (center_x, center_y)
        screen.blit(self.image, self.image_rect)

    def get_image_size(self):
        width = self.image_rect.width
        height = self.image_rect.height
        return width/2, height/2

    def change_image_size(self, rate):
        self.image = pygame.transform.scale(self.image, ((self.image.get_width() * rate), (self.image.get_height() * rate)))
        self.image_rect = self.image.get_rect()

    def return_image_size(self):
        if not self.image.get_size() == self.original_image_size:
            self.image = pygame.transform.scale(self.image, self.original_image_size)
