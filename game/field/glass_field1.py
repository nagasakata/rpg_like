import pygame

from game.field.common_field import CommonField
from game.object.field_object.encount_object import EncountGlass, EncountSwamp
from game.object.field_object.normal_object import Road
from game.object.field_object.unenter_object import BigRock, Lake


class GlassField1(CommonField):
    def __init__(self):
        self.special_object = []

        self.screen = pygame.display.set_mode((0, 0))
        self.screen.fill((153,255,50))
        
        road = Road()
        road.draw(self.screen, 360, 0, 180, 810)

        glass = EncountGlass()
        glass.draw(self.screen, 630, 0, 675, 270)

        swamp = EncountSwamp()
        swamp.draw(self.screen, 630, 450, 675, 360)

        lake = Lake()
        lake.draw(self.screen, 0, 0, 180, 810)


        super().__init__(self.screen, self.special_object)
        

    def set_field(self):
        self.field.blit(self.original_field, (0, 0))

        pygame.display.update()