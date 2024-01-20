import pygame

class SpecialObject():
    def __init__(self):
        pass

    def get_special_object(self):
        object_list = []
        object_list.append(Guild().rect)

        return object_list

    def which_object(self, int):
        if int == 0:
            return Guild



class Guild(SpecialObject):
    def __init__(self):
        self.surface = pygame.image.load("game/object/object_image/ojisan.png").convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.surface.get_width() * 1.6, self.surface.get_height() * 1.6)) 
        self.rect = self.surface.get_rect()