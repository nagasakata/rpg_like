import pygame

def write(screen, font, string:str, place:tuple, color = (255, 255, 255)):
    text = font.render(string, True, color)
    screen.blit(text, place)