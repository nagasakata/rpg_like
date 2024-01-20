import pygame

from game.object.field_object.field_common import FieldCommon

class UnenterObject():
    def __init__(self):
        self.lake = Lake()
        self.bigrock = BigRock()

    def get_unenter_color_list(self):
        object_color_list = []
        object_color_list.append(self.lake.color)
        object_color_list.append(self.bigrock.color)

        return object_color_list

class Lake(FieldCommon):
    def __init__(self):
        self.color = pygame.Color(0, 127, 255)

        super().__init__(self.color)

class BigRock(FieldCommon):
    def __init__(self):
        self.color = pygame.Color(50, 25, 0)

        super().__init__(self.color)
