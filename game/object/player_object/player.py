import pygame
from pygame.locals import *
import sys, copy, random
from game.battle.commoon.battle_script import BattleScript
from game.character.common.friend import Friend
from game.character.common.friend_member import Member
from game.character.human_list.emma.emma import Emma
from game.character.human_list.camila.camila import Camila
from game.field.field_change_manager import FieldManager
from game.item.item_common import add_item
from game.item.weapon.glove.glove_common import GomGlove

from game.object.field_object.encount_object import EncountObject
from game.object.field_object.special_object import Guild, SpecialObject
from game.object.field_object.unenter_object import UnenterObject
from game.object.player_object.player_info import PlayerInfo
from game.object.system_object.guild import guild_menu
from game.object.system_object.menu import Menu

class Player():
    def __init__(self, screen, original_type) -> None:
        self.me_surface = pygame.image.load("game/object/player_object/main_front.png").convert_alpha()
        self.me = self.me_surface.get_rect()
        self.me.center = (450, 45)
        self.screen = screen
        self.original_screen = copy.copy(screen)
        self.original_type = original_type
        self.member = Member()
        Cam = Friend(Camila())
        self.member.add_member(Cam)
        self.member.add_member(Friend(Emma()))
        self.field_manager = FieldManager()
        self.special_object = self.original_type().special_object
        self.special = SpecialObject()
        self.player_info = PlayerInfo()
        self.menu = Menu(self.screen, self.member, self.player_info)
        gg, g2 = GomGlove(), GomGlove()
        Cam.equip_weapon(gg)
        add_item(gg, self.player_info)
        add_item(g2, self.player_info)
        
        
    def get_surface(self):
        return self.me_surface

    def get_dest(self):
        return self.me

    def move(self):

        clock = pygame.time.Clock()

        while True:
            clock.tick(30)
            self.draw()
            pygame.display.update()
            self.key_handler()


    def draw(self):
        self.screen.blit(self.original_screen, (0, 0))
        self.screen.blit(self.get_surface(), self.get_dest())

    def key_handler(self):

        unenter_object = UnenterObject()
        self.me_bottomleft = self.me.bottomleft
        self.me_bottomright = self.me.bottomright
        self.me_topleft = (self.me.bottomleft[0], 2 * self.me.centery - self.me.bottom)
        self.me_topright = (self.me.bottomright[0], 2 * self.me.centery - self.me.bottom)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    if self.me.collidelist(self.special_object) >= 0:
                        if self.special.which_object(self.me.collidelist(self.special_object)) == Guild:
                            self.draw()
                            guild_menu(self.screen, self.member)
                    field_info =  self.field_manager.is_change(self.original_type, self.me.center)
                    if field_info[0]:
                        self.original_type = type(field_info[1])
                        self.special_object = self.original_type().special_object
                        field_info[1].set_field()
                        self.original_screen = copy.copy(field_info[1].screen)
                        if field_info[2] & field_info[3]:
                            self.me.centerx = 35
                        elif (not field_info[2]) & field_info[3]:
                            self.me.centerx = 1245
                        elif field_info[2] & (not field_info[3]):
                            self.me.centery = 35
                        else:
                            self.me.centery = 655
                        self.draw()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_w]: # メニュー
            menu_display = self.menu.indicate()
            self.screen.blit(menu_display, (0, 0))
        else:
            if pressed_keys[K_RIGHT]:
                if self.me.centerx < 1250:
                    self.me_surface = pygame.image.load("game/object/player_object/main_right.png").convert_alpha()
                    if (not self.original_screen.get_at(self.me_topright) in unenter_object.get_unenter_color_list()) & (not self.original_screen.get_at(self.me_bottomright) in unenter_object.get_unenter_color_list()):
                        if pressed_keys[K_d]:
                            self.me.move_ip(7, 0)
                        else:
                            self.me.move_ip(3, 0)
                    self.encount()
            if pressed_keys[K_LEFT]:
                if self.me.centerx > 30:
                    self.me_surface = pygame.image.load("game/object/player_object/main_left.png").convert_alpha()
                    if (not self.original_screen.get_at(self.me_topleft) in unenter_object.get_unenter_color_list()) & (not self.original_screen.get_at(self.me_bottomleft) in unenter_object.get_unenter_color_list()):
                        if pressed_keys[K_d]:
                            self.me.move_ip(-7, 0)
                        else:
                            self.me.move_ip(-3, 0)
                    self.encount()
            if pressed_keys[K_UP]:
                if self.me.centery > 30:
                    self.me_surface = pygame.image.load("game/object/player_object/main_back.png").convert_alpha()
                    if (not self.original_screen.get_at(self.me_topleft) in unenter_object.get_unenter_color_list()) & (not self.original_screen.get_at(self.me_topright) in unenter_object.get_unenter_color_list()):
                        if pressed_keys[K_d]:
                            self.me.move_ip(0, -7)
                        else:
                            self.me.move_ip(0, -3)
                    self.encount()
            if pressed_keys[K_DOWN]:
                if self.me.centery < 660:
                    self.me_surface = pygame.image.load("game/object/player_object/main_front.png").convert_alpha()
                    if (not self.original_screen.get_at(self.me_bottomleft) in unenter_object.get_unenter_color_list()) & (not self.original_screen.get_at(self.me_bottomright) in unenter_object.get_unenter_color_list()):
                        if pressed_keys[K_d]:
                            self.me.move_ip(0, 7)
                        else:
                            self.me.move_ip(0, 3)
                    self.encount()

    def encount(self):
        encount_object = EncountObject()
        now_color = self.original_screen.get_at(self.me.center)
        if now_color in encount_object.get_encount_object_color():
            i = random.randint(1, 10)
            if i == 1:
                now_field = encount_object.color_field(now_color)
                battle_start = BattleScript(self.screen, now_field, self.member, self.player_info)
                battle_start.battle()
                
    


