import pygame, copy
from pygame.locals import *
import sys
from game.item.weapon.weapon_common import Weapon
from game.object.player_object.player_info import PlayerInfo

from game.object.system_object.write import write


class Menu():

    def __init__(self, screen, member, info:PlayerInfo):
        self.screen = screen
        self.original_screen = copy.copy(screen)
        self.member = member
        self.all_member = info.member_all
        self.item = info.item_dict
        self.font = pygame.font.Font("ipaexg.ttf", 27)

    def indicate(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (45, 45, 207, 405))
        
        text_a = self.font.render('パーティー', True, (255, 255, 255))
        text_b = self.font.render('アイテム', True, (255, 255, 255))
        text_c = self.font.render('なにか', True, (255, 255, 255))
        text_d = self.font.render('セーブ', True, (255, 255, 255))
        cursor = self.font.render('->', True, (255, 255, 255))

        self.screen.blit(text_a, (99, 99))
        self.screen.blit(text_b, (99, 189))
        self.screen.blit(text_c, (99, 279))
        self.screen.blit(text_d, (99, 369))
        self.original_menu = copy.copy(self.screen)
        cursor_y = 99
        self.screen.blit(cursor, (65 * 0.9, cursor_y))

        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.screen.blit(self.original_menu, (0,0))
                        if cursor_y == 369:
                            cursor_y = 99
                            self.screen.blit(cursor, (65 * 0.9, cursor_y))
                        else:
                            cursor_y = cursor_y + 90
                            self.screen.blit(cursor, (65 * 0.9, cursor_y))
                    elif event.key == K_UP:
                        self.screen.blit(self.original_menu, (0,0))
                        if cursor_y == 99:
                            cursor_y = 369
                            self.screen.blit(cursor, (65 * 0.9, cursor_y))
                        else:
                            cursor_y = cursor_y - 90
                            self.screen.blit(cursor, (65 * 0.9, cursor_y))
                    elif (event.key == K_RIGHT) | (event.key == K_a):
                        if cursor_y == 99:
                            self.party_menu()
                        elif cursor_y == 189:
                            self.item_menu()
                        elif cursor_y == 279:
                            self.any_menu()
                        elif cursor_y == 369:
                            self.save_menu()
                        self.screen.blit(self.original_menu, (0, 0))
                        self.screen.blit(cursor, (65*0.9, cursor_y))

                    if (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break

        return self.original_screen

    def party_menu(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (270, 99, 288, 315))
        text_a = self.font.render('パーティーの情報', True, (255, 255, 255))
        text_b = self.font.render('パーティーの変更', True, (255, 255, 255))
        text_c = self.font.render('パーティー', True, (255, 255, 255))
        cursor = self.font.render('->', True, (255, 255, 255))
        cursor_y = 153

        self.screen.blit(text_a, (324, 153))
        self.screen.blit(text_b, (324, 243))
        self.screen.blit(text_c, (324, 333))
        original_menu = copy.copy(self.screen)
        self.screen.blit(cursor, (315*0.9, cursor_y))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.screen.blit(original_menu, (0, 0))
                        if cursor_y == 153:
                            self.screen.blit(cursor, (315*0.9, 333))
                            cursor_y = 333
                        else:
                            self.screen.blit(cursor, (315*0.9, cursor_y - 90))
                            cursor_y = cursor_y - 90
                    elif event.key == K_DOWN:
                        self.screen.blit(original_menu, (0, 0))
                        if cursor_y == 333:
                            self.screen.blit(cursor, (315*0.9, 153))
                            cursor_y = 153
                        else:
                            self.screen.blit(cursor, (315*0.9, cursor_y + 90))
                            cursor_y = cursor_y + 90
                    elif (event.key == K_RIGHT) | (event.key == K_a):
                        if cursor_y == 153:
                            self.party_info()
                        elif cursor_y == 243:
                            pass
                        elif cursor_y == 333:
                            pass
                        self.screen.blit(original_menu, (0, 0))
                        self.screen.blit(cursor, (315*0.9, cursor_y))
                    elif (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break

    def party_info(self):
        member_size = len(self.member.member)
        pygame.draw.rect(self.screen, (0, 0, 0), (576, 153, 180, 54 + (member_size - 1)* 45))
        for i in self.member.member:
            text_member = self.font.render(self.member.member[i].get_name(), True, (255, 255, 255))
            self.screen.blit(text_member, (630, 162 + i * 45))
        original_menu = copy.copy(self.screen)
        cursor = self.font.render('->', True, (255, 255, 255))
        cursor_y = 162
        self.screen.blit(cursor, (655*0.9, 162))
        self.one_info((cursor_y - 162) / 50)

        pygame.display.update()
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.screen.blit(original_menu, (0, 0))
                        if cursor_y == 162:
                            self.screen.blit(cursor, (655*0.9, 162 + (member_size - 1) * 45))
                            cursor_y = 162 + (member_size - 1) * 45
                        else:
                            self.screen.blit(cursor, (655*0.9, cursor_y - 45))
                            cursor_y = cursor_y - 45
                        self.one_info((cursor_y - 162) / 45)
                    elif event.key == K_DOWN:
                        self.screen.blit(original_menu, (0, 0))
                        if cursor_y == 162 + (member_size - 1) * 45:
                            self.screen.blit(cursor, (655*0.9, 162))
                            cursor_y = 162
                        else:
                            self.screen.blit(cursor, (655*0.9, cursor_y + 45))
                            cursor_y = cursor_y + 45
                        self.one_info((cursor_y - 162) / 45)
                    elif (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break

    def one_info(self, i:int):
        font2 = pygame.font.Font("ipaexg.ttf", 18)
        pygame.draw.rect(self.screen, (0, 0, 0), (774, 45, 270, 630))
        pygame.draw.rect(self.screen, (0, 0, 0), (1071, 45, 180, 180))
        print(self.member.member[i])
        text_name = font2.render("NAME: " + str(self.member.member[i].get_name()), True, (255, 255, 255))
        text_level = font2.render("LEVEL: " + str(self.member.member[i].get_level()), True, (255, 255, 255))
        text_hp = font2.render("HP: " + str(self.member.member[i].get_hp()), True, (255, 255, 255))
        text_mp = font2.render("MP: " + str(self.member.member[i].get_mp()), True, (255, 255, 255))
        text_attack = font2.render("ATTACK: " + str(self.member.member[i].get_attack()), True, (255, 255, 255))
        text_difence = font2.render("DIFENCE: " + str(self.member.member[i].get_difence()), True, (255, 255, 255))
        text_mattack = font2.render("MAGIC ATTACK: " + str(self.member.member[i].get_magic_attack()), True, (255, 255, 255))
        text_mdifence = font2.render("MAGIC DIFENCE: " + str(self.member.member[i].get_magic_difence()), True, (255, 255, 255))
        text_speed = font2.render("SPEED: " + str(self.member.member[i].get_speed()), True, (255, 255, 255))
        text_experiment = font2.render("Experiment: " + str(self.member.member[i].get_experiment()), True, (255, 255, 255))
        text_next_experiment = font2.render("next: " + str(self.member.member[i].get_next_experiment()), True, (255, 255, 255))
        if self.member.member[i].weapon == None:
            weapon_str = "weapon: None"
        else:
            weapon_str = "weapon: " + str(self.member.member[i].weapon.name) + " Lv" + str(self.member.member[i].weapon.level)
        text_weapon = font2.render(weapon_str, True, (255, 255, 255))

        self.screen.blit(text_name, (792, 90))
        self.screen.blit(text_level, (792, 135))
        self.screen.blit(text_hp, (792, 180))
        self.screen.blit(text_mp, (792, 225))
        self.screen.blit(text_attack, (792, 270))
        self.screen.blit(text_difence, (792, 315))
        self.screen.blit(text_mattack, (792, 360))
        self.screen.blit(text_mdifence, (792, 405))
        self.screen.blit(text_speed, (792, 450))
        self.screen.blit(text_experiment, (792, 495))
        self.screen.blit(text_next_experiment, (792, 540))
        self.screen.blit(text_weapon, (792, 585))
        self.member.member[i].draw_image(self.screen, 1161, 135)


    def item_menu(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (270, 189, 260, 420))
        write(self.screen, self.font, "消費アイテム", (325,252))
        write(self.screen, self.font, "装備", (325,342))
        write(self.screen, self.font, "素材", (325,432))
        write(self.screen, self.font, "大切なもの", (325,522))
        original_menu = copy.copy(self.screen)
        cursor = self.font.render('->', True, (255, 255, 255))
        cursor_y = 252
        self.screen.blit(cursor, (315*0.9, 252))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.screen.blit(original_menu, (0, 0))
                        if cursor_y == 252:
                            self.screen.blit(cursor, (315*0.9, 252 + 270))
                            cursor_y = 252 + 270
                        else:
                            self.screen.blit(cursor, (315*0.9, cursor_y - 90))
                            cursor_y = cursor_y - 90
                    elif event.key == K_DOWN:
                        self.screen.blit(original_menu, (0, 0))
                        if cursor_y == 252 + 270:
                            self.screen.blit(cursor, (315*0.9, 252))
                            cursor_y = 252
                        else:
                            self.screen.blit(cursor, (315*0.9, cursor_y + 90))
                            cursor_y = cursor_y + 90
                    elif event.key == K_a:
                        if cursor_y == 252:
                            self.display_item('consumption')
                        elif cursor_y == 342:
                            self.display_item('weapon')
                        elif cursor_y == 432:
                            self.display_item('material')
                        elif cursor_y == 522:
                            self.display_item('other')
                    if (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break

    def display_item(self, item_type:str):
        original_screen = pygame.Surface.copy(self.screen)
        will_dict = self.item[item_type]
        pygame.draw.rect(self.screen, (0, 0, 0), (550, 50, 300, 600))
        will_dict = self.item[item_type]
        item_id_keys = will_dict.keys()
        item_id_list = list(item_id_keys)
        count, count_item_display, count_weapon = 0, 0, 0
        cursor = self.font.render('->', True, (255, 255, 255))
        cursor_y = 100
        self.screen.blit(cursor, (580, cursor_y))
        if isinstance(will_dict[item_id_list[0]][0], Weapon):
            weapon_list = []
            for i in item_id_list:
                weapon_list = weapon_list + will_dict[item_id_list[0]]
            for j in weapon_list:
                write(self.screen, self.font, j.name + " : Lv" + str(j.level), (620, 100 + 50 * count_item_display))
                count_item_display = count_item_display + 1
        else:
            for i in item_id_list:
                write(self.screen, self.font, will_dict[i][0].name + " : Lv" + str(will_dict[i][1]), (620, 100 + 50 * count_item_display))
            count_item_display = count_item_display + 1
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    count_item_display = 0
                    if (event.key == K_UP):
                        self.screen.blit(original_screen, (0, 0))
                        pygame.draw.rect(self.screen, (0, 0, 0), (550, 50, 300, 600))
                        if isinstance(will_dict[item_id_list[0]][0], Weapon):
                            for i in weapon_list:
                                write(self.screen, self.font, i.name + " : Lv" + str(i.level), (620, 100 + 50 * count_item_display))
                                count_item_display = count_item_display + 1
                        else:
                            for i in item_id_list:
                                write(self.screen, self.font, will_dict[i][0].name + " : Lv" + str(will_dict[i][1]), (620, 100 + 50 * count_item_display))
                                count_item_display = count_item_display + 1
                        if cursor_y == 100:
                            if count <= 0:
                                self.screen.blit(cursor, (580, 100))
                                cursor_y = 100
                            else:
                                self.screen.blit(cursor, (580, 600))
                                cursor_y = 600
                        else:
                            self.screen.blit(cursor, (580, cursor_y - 50))
                            cursor_y = cursor_y - 50
                        if count <= 0:
                            count = 0
                        else:
                            count = count - 1
                    elif (event.key == K_DOWN):
                        self.screen.blit(original_screen, (0, 0))
                        pygame.draw.rect(self.screen, (0, 0, 0), (550, 50, 300, 600))
                        if isinstance(will_dict[item_id_list[0]][0], Weapon):
                            for i in weapon_list:
                                write(self.screen, self.font, i.name + " : Lv" + str(i.level), (620, 100 + 50 * count_item_display))
                                count_item_display = count_item_display + 1
                        else:
                            for i in item_id_list:
                                write(self.screen, self.font, will_dict[i][0].name + " : Lv" + str(will_dict[i][1]), (620, 100 + 50 * count_item_display))
                                count_item_display = count_item_display + 1
                        if cursor_y == 600:
                            self.screen.blit(cursor, (580, 100))
                            cursor_y = 100
                        else:
                            self.screen.blit(cursor, (580, cursor_y + 50))
                            cursor_y = cursor_y + 50
                        if count >= len(item_id_list):
                            count = len(item_id_list)
                        else:
                            count = count + 1
                    if (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break
        self.screen.blit(original_screen, (0, 0))
        pygame.display.update()
        

    def any_menu(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (270, 279, 360, 360))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break

    def save_menu(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (270, 369, 180, 90))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if (event.key == K_LEFT) | (event.key == K_q):
                        break
            else:
                pygame.display.update()
                continue
            break
