import pygame
from pygame import Rect

class FieldCommon(Rect):
    def __init__(self, color) -> None:
        self.color = color

    def draw(self, screen, left:int, top:int, height:int, width:int):
        pygame.draw.rect(screen, self.color, [left, top, height, width])
