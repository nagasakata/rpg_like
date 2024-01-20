import sys
import pygame
import copy
from pygame.locals import *
from game.battle.commoon.attack import Attack
from game.battle.commoon.spell_common import Spell
from game.character.common.enemy import Enemy
from game.character.common.friend import Friend

from game.character.common.friend_member import Member
from game.item.item_common import add_item
from game.object.player_object.player_info import PlayerInfo
from game.object.system_object.write import write

class BattleScript():
    def __init__(self, screen, field, member, info:PlayerInfo) -> None:
        self.screen = screen
        self.original_screen = copy.copy(self.screen)
        self.member = member
        self.field = field
        self.action_order = []
        self.turn_count = 1
        self.finish = True #逃げた場合、もしくは戦闘そのものがおわった場合False
        self.fin = False #一人のターンが終わったときTrue
        self.done = False #何か画面に変化があるときTrue
        self.cursor_count = 1
        self.experiment_all = 0
        self.enemies = self.field.enemy_member
        self.text_counter = 0
        self.info = info
        self.money = 0


# 画面に変化がある時呼ぶ
    def make_original(self):

        self.screen.fill((0, 0, 0))
        pygame.draw.line(self.screen, (255, 255, 255), (0, 600 * 0.85), (1500 * 0.85, 600 * 0.85))
        pygame.draw.line(self.screen, (255, 255, 255), (400 * 0.85, 0), (400 * 0.85, 900 * 0.85))
        pygame.draw.line(self.screen, (255, 255, 255), (0, 150 * 0.85), (400 * 0.85, 150 * 0.85))
        pygame.draw.line(self.screen, (255, 255, 255), (0, 300 * 0.85), (400 * 0.85, 300 * 0.85))
        pygame.draw.line(self.screen, (255, 255, 255), (0, 450 * 0.85), (400 * 0.85, 450 * 0.85))

        self.font = pygame.font.Font("ipaexg.ttf", 25)

        for i in self.member.member:
            text_name = self.font.render(self.member.member[i].get_name(), True, (255, 255, 255))
            text_hp = self.font.render("HP: " + str(self.member.member[i].get_hp()), True, (255, 255, 255))
            text_mp = self.font.render("MP: " + str(self.member.member[i].get_mp()), True, (255, 255, 255))
            self.screen.blit(text_name, (50 * 0.85, 10 * 0.85 + i * 150 * 0.85))
            self.screen.blit(text_hp, (50 * 0.85, 55 * 0.85 + i * 150 * 0.85))
            self.screen.blit(text_mp, (50 * 0.85, 100 * 0.85 + i * 150 * 0.85))
            self.member.member[i].draw_image(self.screen, 300 *0.85, 75 * 0.85 + i * 150 * 0.85)

        text_attack = self.font.render("こうげき", True, (255, 255, 255))
        text_skill = self.font.render("こうどう", True, (255, 255, 255))
        text_item = self.font.render("アイテム", True, (255, 255, 255))
        text_run = self.font.render("にげる", True, (255, 255, 255))
        self.screen.blit(text_attack, (250 * 0.85, 625 * 0.85))
        self.screen.blit(text_skill, (250 * 0.85, 665 * 0.85))
        self.screen.blit(text_item, (250 * 0.85, 705 * 0.85))
        self.screen.blit(text_run, (250 * 0.85, 745 * 0.85))

        self.enemy_print()

        self.original_battle = copy.copy(self.screen)
        pygame.display.update()

    def battle(self):
        self.make_original()
        self.money = 0

        self.make_action_order(self.member.member, self.enemies.enemies)
        self.turn_count = 1

        while True:
            if not self.finish:
                break
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if not self.finish:
                        break
                    if event.key == K_a:
                        for turn in self.action_order:
                            if self.finish:
                                self.done = False
                                self.fin = False
                                if isinstance(turn, Friend):
                                    self.friend_turn(turn)
                                elif isinstance(turn, Enemy):
                                    self.enemy_turn(turn)
                                if self.done:
                                    self.make_original()
                                self.screen.blit(self.original_battle, (0, 0))
                                if len(self.enemies.enemies) == 0:
                                    print("you win!")
                                    growth_dict = self.member.win_experiment(self.experiment_all)
                                    self.info.add_money(self.money)
                                    self.finish = False
                                    for i in growth_dict:
                                        if growth_dict[i]['level_bool']:
                                            self.level_up(i, growth_dict[i])
                                elif len(self.member.member) == 0:
                                    print("you lose")
                                    self.finish = False
                            else:
                                break
                        else:
                            continue
                        break
                    self.turn_count = self.turn_count + 1
                    self.screen.blit(self.original_battle, (0, 0))
            else:
                continue
            break

    # 改善の余地あり
    def level_up(self, name, growth_dict):
        text_level_name = self.font.render(name + " level up !   level: + " + str(growth_dict['level']), True, (255, 255, 255))
        text_level_hp = self.font.render("hp: + " + str(growth_dict['hp']), True, (255, 255, 255))
        text_level_mp = self.font.render("mp: + " + str(growth_dict['mp']), True, (255, 255, 255))
        text_level_attack = self.font.render("attack: + " + str(growth_dict['attack']), True, (255, 255, 255))
        text_level_difence = self.font.render("difence: + " + str(growth_dict['difence']), True, (255, 255, 255))
        text_level_mattack = self.font.render("magic attack: + " + str(growth_dict['magic_attack']), True, (255, 255, 255))
        text_level_mdifence = self.font.render("magic difence: + " + str(growth_dict['magic_difence']), True, (255, 255, 255))
        text_level_speed = self.font.render("speed: + " + str(growth_dict['speed']), True, (255, 255, 255))

        self.screen.blit(self.original_battle, (0, 0))
        self.screen.blit(text_level_name, (400, 550))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        if self.text_counter == 0:
                            pygame.display.update()
                            self.screen.blit(self.original_battle, (0, 0))
                            self.screen.blit(text_level_hp, (400, 550))
                            self.screen.blit(text_level_mp, (400, 620))
                            self.screen.blit(text_level_attack, (550, 550))
                            self.screen.blit(text_level_difence, (550, 620))
                            self.screen.blit(text_level_mattack, (750, 550))
                            self.screen.blit(text_level_mdifence, (750, 620))
                            self.screen.blit(text_level_speed, (1000, 550))
                            if growth_dict['skill'][0]:
                                self.text_counter = 1
                            else:
                                self.text_counter = 2
                        elif self.text_counter == 1:
                            if growth_dict['skill'][0]:
                                self.text_counter = 0
                                while True:
                                    pygame.display.update()
                                    for event2 in pygame.event.get():
                                        if event2.type == QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        if event2.type == KEYDOWN:
                                            if event2.key == K_a:
                                                if len(growth_dict['skill'][1]) == self.text_counter:
                                                    self.text_counter = 2
                                                    break
                                                else:
                                                    self.screen.blit(self.original_battle, (0, 0))
                                                    text_skill = self.font.render(name + " learned new skill: " + growth_dict['skill'][1][self.text_counter], True, (255, 255, 255))
                                                    self.screen.blit(text_skill, (400, 550))
                                                    self.text_counter = self.text_counter + 1
                                    else:
                                        continue
                                    break
                            self.text_counter = 2

                        else:
                            self.text_counter = 0
                            self.screen.blit(self.original_battle, (0, 0))
                            break
            else:
                continue
            break

    def enemy_print(self):
        enemy_many = len(self.enemies.enemies)
        for enemy_id in self.enemies.enemies:
            enemy_size = self.enemies.enemies[enemy_id].get_image_size()
            text_name = self.font.render(self.enemies.enemies[enemy_id].get_name(), True, (255, 255, 255))
            text_hp = self.font.render("HP: " + str(self.enemies.enemies[enemy_id].get_hp()), True, (255, 255, 255))
            if enemy_many == 1:
                self.enemies.enemies[enemy_id].draw_image(self.screen, 930 * 0.85, 300 * 0.85)
                self.screen.blit(text_name, (880 * 0.85, 310 * 0.85 + enemy_size[1]))
                self.screen.blit(text_hp, (880 * 0.85, 350 * 0.85 + enemy_size[1]))
            elif enemy_many == 2:
                self.enemies.enemies[enemy_id].draw_image(self.screen, 320 * 0.85 + enemy_id * 400 * 0.85, 300 * 0.85)
                self.screen.blit(text_name, (270 * 0.85 + enemy_id * 400 * 0.85, 310 * 0.85 + enemy_size[1]))
                self.screen.blit(text_hp, (270 * 0.85 + enemy_id * 400 * 0.85, 350 * 0.85 + enemy_size[1]))
            elif enemy_many == 3:
                self.enemies.enemies[enemy_id].draw_image(self.screen, 320 * 0.85 + enemy_id * 300 * 0.85, 300 * 0.85)
                self.screen.blit(text_name, (270 * 0.85 + enemy_id * 300 * 0.85, 310 * 0.85 + enemy_size[1]))
                self.screen.blit(text_hp, (270 * 0.85 + enemy_id * 300 * 0.85, 350 * 0.85 + enemy_size[1]))
            elif enemy_many == 4:
                if enemy_id <= 2:
                    self.enemies.enemies[enemy_id].draw_image(self.screen, 410 * 0.85 + enemy_id * 400 * 0.85, 150 * 0.85)
                    self.screen.blit(text_name, (360 * 0.85 + enemy_id * 400 * 0.85, 160 * 0.85 + enemy_size[1]))
                    self.screen.blit(text_hp, (360 * 0.85 + enemy_id * 400 * 0.85, 200 * 0.85 + enemy_size[1]))
                else:
                    self.enemies.enemies[enemy_id].draw_image(self.screen, 610 * 0.85 + (enemy_id - 3) * 400 * 0.85, 390 * 0.85)
                    self.screen.blit(text_name, (560 * 0.85 + (enemy_id - 3) * 400 * 0.85, 400 * 0.85 + enemy_size[1]))
                    self.screen.blit(text_hp, (560 * 0.85 + (enemy_id - 3) * 400 * 0.85, 440 * 0.85 + enemy_size[1]))
            elif enemy_many == 5:
                if enemy_id <= 2:
                    self.enemies.enemies[enemy_id].draw_image(self.screen, 320 * 0.85 + enemy_id * 400 * 0.85, 150 * 0.85)
                    self.screen.blit(text_name, (270 * 0.85 + enemy_id * 400 * 0.85, 160 * 0.85 + enemy_size[1]))
                    self.screen.blit(text_hp, (270 * 0.85 + enemy_id * 400 * 0.85, 200 * 0.85 + enemy_size[1]))
                else:
                    self.enemies.enemies[enemy_id].draw_image(self.screen, 250 * 0.85 + (enemy_id - 2) * 350 * 0.85, 390 * 0.85)
                    self.screen.blit(text_name, (170 * 0.85 + (enemy_id - 2) * 350 * 0.85, 400 * 0.85 + enemy_size[1]))
                    self.screen.blit(text_hp, (170 * 0.85 + (enemy_id - 2) * 350 * 0.85, 440 * 0.85 + enemy_size[1]))

    def make_action_order(self, f_member:dict, e_member:dict):
        self.action_order = []
        for e in e_member:
            pre_order = []
            count = 1
            if len(self.action_order) == 0:
                self.action_order.append(e_member[e])
            else:
                for i in self.action_order:
                    if count == (len(self.action_order)):
                        pre_order.append(i)
                        if i.get_speed() >= e_member[e].get_speed():
                            self.action_order = pre_order + [e_member[e]]
                        else:
                            self.action_order = pre_order[0:count-1] + [e_member[e]] + pre_order[-1:]

                    elif i.get_speed() <= e_member[e].get_speed():
                        self.action_order = pre_order + [e_member[e]] + self.action_order[-(len(self.action_order) - count + 1):]
                        break
                    else:
                        pre_order.append(i)
                        count = count + 1

        for f in f_member:
            pre_order = []
            count = 1
            for i in self.action_order:
                if count == (len(self.action_order)):
                    pre_order.append(i)
                    if i.get_speed() >= f_member[f].get_speed():
                        self.action_order = pre_order + [f_member[f]]
                    else:
                        self.action_order = pre_order[0:count-1] + [f_member[f]] + pre_order[-1:]
                elif i.get_speed() <= f_member[f].get_speed():
                    self.action_order = pre_order + [f_member[f]] + self.action_order[-(len(self.action_order) - count + 1):]
                    break
                else:
                    pre_order.append(i)
                    count = count + 1

        return self.action_order

    def enemy_turn(self, turn):
        text_start = self.font.render(turn.get_name(), True, (255, 255, 255))
        self.screen.blit(text_start, (48 * 0.85, 625 * 0.85))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        break
            else:
                continue
            break

    def friend_turn(self, turn):
        turn.draw_image(self.screen, 100 * 0.85, 720 * 0.85)
        friend_turn_original = copy.copy(self.screen)
        cursor = self.font.render("->", True, (255, 255, 255))
        cursor_y = 625 * 0.85
        self.screen.blit(cursor, (200 * 0.85, cursor_y))
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.screen.blit(friend_turn_original, (0, 0))
                        if cursor_y == 625 * 0.85:
                            cursor_y = 745 * 0.85
                        else:
                            cursor_y = cursor_y - 40 * 0.85
                        self.screen.blit(cursor, (200 * 0.85, cursor_y))
                    elif event.key == K_DOWN:
                        self.screen.blit(friend_turn_original, (0, 0))
                        if cursor_y == 745 * 0.85:
                            cursor_y = 625 * 0.85
                        else:
                            cursor_y = cursor_y + 40 * 0.85
                        self.screen.blit(cursor, (200 * 0.85, cursor_y))
                    elif event.key == K_a:
                        if cursor_y == 625 * 0.85:
                            self.attack(turn)
                        elif cursor_y == 665 * 0.85:
                            self.use_skill(turn)
                        elif cursor_y == 705 * 0.85:
                            self.use_item(turn)
                        elif cursor_y == 745 * 0.85:
                            self.run_away()

                    if self.fin:
                        break
            else:
                continue
            break

    def attack(self, turn_player, skill = None):
        original_attack = copy.copy(self.screen)
        self.cursor_count = 1
        enemy_many = len(self.enemies.enemies)
        self.display_cursor_initial(enemy_many)
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.display_cursor(enemy_many, K_RIGHT, original_attack)
                    elif event.key == K_LEFT:
                        self.display_cursor(enemy_many, K_LEFT, original_attack)
                    elif event.key == K_a:
                        if skill == None:
                            attack_script = Attack(turn_player, self.enemies.enemies[self.cursor_count])
                            if attack_script.do_attack():
                                self.experiment_all = self.experiment_all + self.enemies.enemies[self.cursor_count].get_experiment()
                                self.money = self.money + self.enemies.enemies[self.cursor_count].money
                                add_item(self.enemies.enemies[self.cursor_count].get_item(), self.info)
                                self.enemies.kill_enemy(self.enemies.enemies[self.cursor_count])
                            self.done = True
                            self.fin = True
                        elif isinstance(skill, Spell):
                            if skill.use_spell(turn_player, self.enemies.enemies[self.cursor_count]):
                                self.experiment_all = self.experiment_all + self.enemies.enemies[self.cursor_count].get_experiment()
                                self.money = self.money + self.enemies.enemies[self.cursor_count].money
                                add_item(self.enemies.enemies[self.cursor_count].get_item(), self.info)
                                self.enemies.kill_enemy(self.enemies.enemies[self.cursor_count])
                            self.done = True
                            self.fin = True
                        break
                    elif event.key == K_q:
                        break
            else:
                continue
            break
        self.screen.blit(original_attack, (0, 0))

    def display_cursor_initial(self, enemy_many):
        cursor = self.font.render("→", True, (255, 255, 255))
        enemy_size = self.enemies.enemies[1].get_image_size()
        if enemy_many == 1:
            self.screen.blit(cursor, (830 * 0.85, 310 * 0.85 + enemy_size[1]))
        elif enemy_many == 2:
            self.screen.blit(cursor, (620 * 0.85, 310 * 0.85 + enemy_size[1]))
        elif enemy_many == 3:
            self.screen.blit(cursor, (520 * 0.85, 310 * 0.85 + enemy_size[1]))
        elif enemy_many == 4:
            self.screen.blit(cursor, (710 * 0.85, 160 * 0.85 + enemy_size[1]))
        elif enemy_many == 5:
            self.screen.blit(cursor, (620 * 0.85, 160 * 0.85 + enemy_size[1]))

    def display_cursor(self, enemy_many:int, key, original):
        self.screen.blit(original, (0, 0))
        cursor = self.font.render("→", True, (255, 255, 255))
        if enemy_many == 1:
            enemy_size = self.enemies.enemies[1].get_image_size()
            self.screen.blit(cursor, (830 * 0.85, 310 * 0.85 + enemy_size[1]))
        elif enemy_many == 2:
            if self.cursor_count == 2:
                self.cursor_count = self.cursor_count - 1
                enemy_size = self.enemies.enemies[self.cursor_count].get_image_size()
                self.screen.blit(cursor, (620 * 0.85, 310 * 0.85 + enemy_size[1]))
            else:
                self.cursor_count = self.cursor_count + 1
                enemy_size = self.enemies.enemies[self.cursor_count].get_image_size()
                self.screen.blit(cursor, (1020 * 0.85, 310 * 0.85 + enemy_size[1]))
        elif enemy_many == 3:
            if key == K_LEFT:
                if self.cursor_count == 1:
                    self.cursor_count = 3
                else:
                    self.cursor_count = self.cursor_count - 1
                enemy_size = self.enemies.enemies[self.cursor_count].get_image_size()
                self.screen.blit(cursor, (220 * 0.85 + self.cursor_count * 300 * 0.85, 310 * 0.85 + enemy_size[1]))
            elif key == K_RIGHT:
                if self.cursor_count == 3:
                    self.cursor_count = 1
                else:
                    self.cursor_count = self.cursor_count + 1
                enemy_size = self.enemies.enemies[self.cursor_count].get_image_size()
                self.screen.blit(cursor, (220 * 0.85 + self.cursor_count * 300 * 0.85, 310 * 0.85 + enemy_size[1]))
        elif enemy_many == 4:
            if key == K_LEFT:
                if self.cursor_count == 1:
                    self.cursor_count = 4
                else:
                    self.cursor_count = self.cursor_count - 1
            elif key == K_RIGHT:
                if self.cursor_count == 4:
                    self.cursor_count = 1
                else:
                    self.cursor_count = self.cursor_count + 1
            enemy_size = self.enemies.enemies[self.cursor_count].get_image_size()
            if self.cursor_count <= 2:
                self.screen.blit(cursor, (310 * 0.85 + self.cursor_count * 400 * 0.85, 160 * 0.85 + enemy_size[1]))
            else:
                self.screen.blit(cursor, (510 * 0.85 + (self.cursor_count - 3) * 400 * 0.85, 400 * 0.85 + enemy_size[1]))
        elif enemy_many == 5:
            if key == K_LEFT:
                if self.cursor_count == 1:
                    self.cursor_count = 5
                else:
                    self.cursor_count = self.cursor_count - 1
            elif key == K_RIGHT:
                if self.cursor_count == 5:
                    self.cursor_count = 1
                else:
                    self.cursor_count = self.cursor_count + 1
            enemy_size = self.enemies.enemies[self.cursor_count].get_image_size()
            if self.cursor_count <= 2:
                self.screen.blit(cursor, (220 * 0.85 + self.cursor_count * 400 * 0.85, 160 * 0.85 + enemy_size[1]))
            else:
                self.screen.blit(cursor, (120 * 0.85 + (self.cursor_count - 2) * 350 * 0.85, 400 * 0.85 + enemy_size[1]))
        


    def use_skill(self, turn):
        original = copy.copy(self.screen)
        text_spell = self.font.render("スペル", True, (255, 255, 255))
        text_skill = self.font.render("スキル", True, (255, 255, 255))
        text_guard = self.font.render("ぼうぎょ", True, (255, 255, 255))
        self.screen.blit(text_spell, (470 * 0.85, 625 * 0.85))
        self.screen.blit(text_skill, (470 * 0.85, 665 * 0.85))
        self.screen.blit(text_guard, (470 * 0.85, 705 * 0.85))
        pygame.draw.line(self.screen, (255, 255, 255), (600 * 0.85, 600 * 0.85), (600 * 0.85, 900 * 0.85))
        skill_original = copy.copy(self.screen)

        cursor = self.font.render("->", True, (255, 255, 255))
        cursor_y = 625 * 0.85
        self.screen.blit(skill_original, (0, 0))
        self.screen.blit(cursor, (425 * 0.85, 620 * 0.85))

        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        if cursor_y == 705 * 0.85:
                            cursor_y = 625 * 0.85
                        else:
                            cursor_y = cursor_y + 40 * 0.85
                        self.screen.blit(skill_original, (0, 0))
                        self.screen.blit(cursor, (425 * 0.85, cursor_y))
                    elif event.key == K_UP:
                        if cursor_y == 625 * 0.85:
                            cursor_y = 705 * 0.85
                        else:
                            cursor_y = cursor_y - 40 * 0.85
                        self.screen.blit(skill_original, (0, 0))
                        self.screen.blit(cursor, (425 * 0.85, cursor_y))
                    elif event.key == K_a:
                        if cursor_y == 625 * 0.85:
                            self.select_skill(turn, Spell)
                            if self.fin:
                                break
                        elif cursor_y == 665 * 0.85:
                            pass
                        elif cursor_y == 700 * 0.85:
                            pass
                    elif event.key == K_q:
                        break
            else:
                continue
            break
        self.screen.blit(original, (0, 0))
        pygame.display.update()

    def select_skill(self, turn, type):
        before = copy.copy(self.screen)
        write_list = []
        
        for skill in turn.skill_list:
            if isinstance(turn.skill_list[skill], type):
                write_list.append(turn.skill_list[skill])

        skill_size = len(write_list)

        if not skill_size == 0:

            skill_count, text_x, text_y = 0, 0, 0
            for i in write_list:
                text_y = (625 + (skill_count % 4) * 40) * 0.85
                text_x = (700 + skill_count // 4 * 250) * 0.85
                write(self.screen, self.font, i.get_name(), (text_x, text_y))
                skill_count = skill_count  + 1

            skill_original = copy.copy(self.screen)
            cursor_x, cursor_y = 650 * 0.85, 625 * 0.85
            write(self.screen, self.font, "->", (cursor_x, cursor_y))
            pygame.display.update()

            skill_count = 0
            skill_count_x, skill_count_y = 0, 0
            skill_size = skill_size - 1
            skill_last = skill_size - skill_size % 4

            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        self.screen.blit(skill_original, (0, 0))
                        print(cursor_y)
                        if event.key == K_DOWN:
                            if skill_count < skill_last:
                                if cursor_y == 745 * 0.85:
                                    cursor_y = 625 * 0.85
                                    skill_count = skill_count - 3
                                else:
                                    cursor_y = cursor_y + 40 * 0.85
                                    skill_count = skill_count + 1
                            else:
                                if cursor_y == (625 + 40 * (skill_size % 4)) * 0.85:
                                    cursor_y = 625 * 0.85
                                    skill_count = skill_count - skill_size % 4
                                else:
                                    cursor_y = cursor_y + 40 * 0.85
                                    skill_count = skill_count + 1
                            write(self.screen, self.font, "->", (cursor_x, cursor_y))
                        elif event.key == K_UP:
                            if skill_count < skill_last:
                                if cursor_y == 625 * 0.85:
                                    cursor_y = 745 * 0.85
                                    skill_count = skill_count + 3
                                else:
                                    cursor_y = cursor_y - 40 * 0.85
                                    skill_count = skill_count - 1
                            else:
                                if cursor_y == 625 * 0.85:
                                    cursor_y = (625 + 40 * (skill_size % 4)) * 0.85
                                    skill_count = skill_count + skill_size % 4
                                else:
                                    cursor_y = cursor_y - 40 * 0.85
                                    skill_count = skill_count - 1
                            write(self.screen, self.font, "->", (cursor_x, cursor_y))
                        elif event.key == K_RIGHT:
                            if skill_count < skill_last:
                                if cursor_x == 1150 * 0.85:
                                    pass
                                else:
                                    if skill_count + 4 <= skill_size:
                                        cursor_x = cursor_x + 250 * 0.85
                                        skill_count = skill_count + 4
                            else:
                                pass # スキルが１３個以上のとき必要　必要になったら追加する（面倒くさい）
                            write(self.screen, self.font, "->", (cursor_x, cursor_y))
                        elif event.key == K_LEFT:
                            if skill_count <= 11:
                                if cursor_x == 650 * 0.85:
                                    pass
                                else:
                                    cursor_x = cursor_x - 250 * 0.85
                                    skill_count = skill_count - 4
                            else:
                                pass # スキルが１３個以上のとき必要　必要になったら追加する（面倒くさい）
                            write(self.screen, self.font, "->", (cursor_x, cursor_y))
                        elif event.key == K_a:
                            self.attack(turn, write_list[skill_count])
                            break
                        elif event.key == K_q:
                            break
                        print(skill_count)
                        pygame.display.update()
                else:
                    continue
                break
            self.screen.blit(before, (0, 0))
            pygame.display.update()

    def use_item(self, turn):
        pass

    def run_away(self):
        self.finish = False
        self.fin = True


