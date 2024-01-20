import pygame

from game.field.common_field import CommonField
from game.object.field_object.normal_object import Road
from game.object.field_object.special_object import Guild
from game.object.field_object.unenter_object import Lake

class Village1(CommonField):
    def __init__(self):
        self.special_object = []

        self.screen = pygame.display.set_mode((0, 0))
        self.screen.fill((153,255,50))

        road = Road()
        road.draw(self.screen, 360, 0, 180, 500)
        road.draw(self.screen, 0, 500, 540, 180)
        
        lake = Lake()
        lake.draw(self.screen, 0, 0, 180, 250)

        self.add_object_rect(Guild(), (450, 300))
        
        super().__init__(self.screen, self.special_object)



        
    def set_field(self):
        self.field.blit(self.original_field, (0, 0))
        self.add_object(Guild(), (450, 300))
        pygame.display.update()