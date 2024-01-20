import pygame
from pygame.locals import *
import sys
from game.character.common.friend import Friend
from game.character.common.friend_member import Member
from game.character.common.mob_human import Mob

from game.object.system_object.write import write


def guild_menu(screen, member:Member):
    font = pygame.font.Font("ipaexg.ttf", 27)
    pygame.draw.rect(screen, (0, 0, 0), (55, 55, 207, 205))
    write(screen, font, "ギルドメニュー", (60, 100))
    write(screen, font, "雇う", (100, 150))
    write(screen, font, "入れ替える", (100, 200))
    original_screen = pygame.Surface.copy(screen)

    cursor = font.render('->', True, (255, 255, 255))
    cursor_y = 150
    screen.blit(cursor, (70, cursor_y))

    while True:
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                screen.blit(original_screen, (0, 0))
                if (event.key == K_UP) | (event.key == K_DOWN):
                    if cursor_y == 150:
                        cursor_y = 200
                    elif cursor_y == 200:
                        cursor_y = 150
                    screen.blit(cursor, (70, cursor_y))
                if event.key == K_a:
                    if cursor_y == 150:
                        screen.blit(cursor, (70, cursor_y))
                        hire(screen, member)
                    elif cursor_y == 200:
                        pass
                elif event.key == K_q:
                    break
        else:
            continue
        break

def hire(screen, member:Member):
    original = pygame.Surface.copy(screen)
    font = pygame.font.Font("ipaexg.ttf", 27)
    font2 = pygame.font.Font("ipaexg.ttf", 25)
    pygame.draw.rect(screen, (0, 0, 0), (55, 280, 207, 315))
    write(screen, font2, "今雇えるのは", (75, 300))
    write(screen, font2, "こいつらだぜ", (75, 335))

    mob_a = Mob()
    mob_b = Mob()
    mob_c = Mob()
    mob_d = Mob()

    write(screen, font, "一人目", (150, 385))
    write(screen, font, "二人目", (150, 435))
    write(screen, font, "三人目", (150, 485))
    write(screen, font, "四人目", (150, 535))
    
    original_screen = pygame.Surface.copy(screen)
    
    cursor = font.render('->', True, (255, 255, 255))
    cursor_y = 385
    screen.blit(cursor, (105, cursor_y))
    display_mob(screen, cursor_y, mob_a, mob_b, mob_c, mob_d)
    
    while True:
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                screen.blit(original_screen, (0, 0))
                if event.key == K_UP:
                    if cursor_y == 385:
                        cursor_y = 535
                    else:
                        cursor_y = cursor_y - 50
                    screen.blit(cursor, (105, cursor_y))
                    display_mob(screen, cursor_y, mob_a, mob_b, mob_c, mob_d)
                elif event.key == K_DOWN:
                    if cursor_y == 535:
                        cursor_y = 385
                    else:
                        cursor_y = cursor_y + 50
                    screen.blit(cursor, (105, cursor_y))
                    display_mob(screen, cursor_y, mob_a, mob_b, mob_c, mob_d)
                elif event.key == K_a:
                    if cursor_y == 385:
                        mob = mob_a
                    elif cursor_y == 435:
                        mob = mob_b
                    elif cursor_y == 485:
                        mob = mob_c
                    elif cursor_y == 535:
                        mob = mob_d
                    if not ((0 in member.member) & (1 in member.member) & (2 in member.member) & (3 in member.member)):
                        new_name = input("新しい名前を入力してください: ")
                        mob.set_name(new_name)
                        member.add_member(Friend(mob))
                        break
                elif event.key == K_q:
                    break
        else:
            continue
        break
    screen.blit(original, (0, 0))
    pygame.display.update()

def display_mob(screen, cursor_y, mob_a, mob_b, mob_c, mob_d):
    mob:Mob = None
    if cursor_y == 385:
        mob = mob_a
    elif cursor_y == 435:
        mob = mob_b
    elif cursor_y == 485:
        mob = mob_c
    elif cursor_y == 535:
        mob = mob_d

    font2 = pygame.font.Font("ipaexg.ttf", 25)
    pygame.draw.rect(screen, (0, 0, 0), (600, 45, 290, 650))
    pygame.draw.rect(screen, (0, 0, 0), (920, 45, 180, 180))
    mob.draw_image(screen, 1010, 135)
    write(screen, font2, "hp : " + str(mob.hp), (630, 70))
    write(screen, font2, "mp : " + str(mob.mp), (630, 110))
    write(screen, font2, "attack : " + str(mob.attack), (630, 150))
    write(screen, font2, "difence : " + str(mob.difence), (630, 190))
    write(screen, font2, "magic attack : " + str(mob.magic_attack), (630, 230))
    write(screen, font2, "magic difence : " + str(mob.magic_difence), (630, 270))
    write(screen, font2, "speed : " + str(mob.speed), (630, 310))
        
