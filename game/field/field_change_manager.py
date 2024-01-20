import pygame

from game.field.common_field import CommonField
from game.field.glass_field1 import GlassField1
from game.field.glass_field2 import GlassField2
from game.field.village1 import Village1


class FieldManager():
    def __init__(self):
        self.change_list = []

    def change_field_list(self):
        self.change_range(GlassField1(), Village1(), True, change_y = 660, range_x = (360, 540))
        self.change_range(Village1(), GlassField1(), False, change_y = 30, range_x = (360, 540))
        self.change_range(GlassField1(), GlassField2(), False, change_y = 30, range_x = (360, 540))
        self.change_range(GlassField2(), GlassField1(), True, change_y = 660, range_x = (360, 540))


    def is_change(self, field, place):
        self.change_field_list()
        enough_range = 10
        changable = False
        to_change = None
        plus = False
        x = False
        for i in self.change_list:
            if field == type(i[2]):
                if i[5]:
                    if i[4]:
                        if (place[0] >= i[0] - enough_range) & (place[1] >= i[1][0]) & (place[1] <= i[1][1]):
                            changable = True
                    else:
                        if (place[0] <= i[0] + enough_range) & (place[1] >= i[1][0]) & (place[1] <= i[1][1]):
                            changable = True
                else:
                    if i[4]:
                        if (place[0] >= i[0][0]) & (place[0] <= i[0][1]) & (place[1] >= i[1] - enough_range):
                            changable = True
                    else:
                        if (place[0] >= i[0][0]) & (place[0] <= i[0][1]) & (place[1] <= i[1] + enough_range):
                            changable = True
            if changable:
                to_change = i[3]
                plus = i[4]
                x = i[5]
                break
        return changable, to_change, plus, x


    def change_range(self, change_before:CommonField, change_after:CommonField, plus:bool, change_x = None, range_y = None, change_y = None, range_x = None):
        if not change_x == None:
            self.change_list.append((change_x, range_y, change_before, change_after, plus, True))
        elif not change_y == None:
            self.change_list.append((range_x, change_y, change_before, change_after, plus, False))