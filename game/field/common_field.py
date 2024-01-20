import pygame, copy

from game.object.field_object.special_object import SpecialObject

class CommonField():
    def __init__(self, field, special_object):
        self.field = field
        self.original_field = copy.copy(field)
        self.special_object = special_object

    def add_object(self, object:SpecialObject, place):
        object.rect.center = place
        self.field.blit(object.surface, object.rect)
        self.special_object.append(object.rect)

    def add_object_rect(self, object:SpecialObject, place):
        object.rect.center = place
        self.special_object.append(object.rect)
