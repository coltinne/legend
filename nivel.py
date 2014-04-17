#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from config import Config
from objetos.objetos import *
from objetos.personagem import *


class Nivel():
    def __init__(self):
        self.config = Config()
        self.sprite_ambiente = pygame.sprite.Group()
        self.sprite_porta = pygame.sprite.Group()
        self.sprite_inimigos = pygame.sprite.Group()

        self.fase = 0
        self.level = []

        self.level_modelo()
        self.nivel()
    #__init__

    def level_modelo(self):
        if self.fase == 0:
            self.level = [
                "TTTTTTTTTTTTTTTTTTTTTTTTT",
                "E-----------------------E",
                "E--------------------P--E",
                "E-------------------BBBBE",
                "E-------------BBBBBBB---E",
                "E-------BBBBBBB---------E",
                "EBB---------------------E",
                "E-BBBB------------------E",
                "E-----BBBBB-------------E",
                "E-----------------------E",
                "E-------------BBBBBBBB--E",
                "EBBBBBBBB---------------E",
                "E-----------------------E",
                "E-----------BBBBBB------E",
                "EBBBBBB-----------------E",
                "E-----------------------E",
                "E------BBBBBB-----------E",
                "E-----------------------E",
                "ESSSSSSSSSSSSSSSSSSSSSSSE", ]
        elif self.fase == 1:
            self.level = [
                "TTTTTTTTTTTTTTTTTTTTTTTTT",
                "E-------P-----B---------E",
                "E--B-BBBBBBB--B---------E",
                "E-B--B-BB-----B---------E",
                "E---------BBBBBBBBBBBB--E",
                "E0BBBBBBB--B---BB----BB-E",
                "E----------------B------E",
                "E----------BB---BBB--BBBE",
                "EBBBBBBBBBBB--B-B-BB----E",
                "E-------------BB--BBBBB-E",
                "E-B-BBBBBBBBBBBBBBB-----E",
                "E-----------------B-B---E",
                "EBBBBBBBBBB-B-BBBB---BBBE",
                "E---------B---B-B-------E",
                "EBBBBBBBB---BBBBBBBBBB-BE",
                "E------------------B----E",
                "E------BB-----B---------E",
                "E-------------BBBBBBBBBBE",
                "ESSSSSSSSSSSSSSSSSSSSSSSS", ]
    #level

    def next_nivel(self):
        self.fase += 1
        self.esvaziar_sprites()
        self.level_modelo()
        self.nivel()
    #next nivel

    def prev_nivel(self):
        self.fase -= 1
        self.esvaziar_sprites()
        self.level_modelo()
        self.nivel()
    #prev nivel

    def nivel(self):
        x = y = 0
        for i in self.level:
            for j in i:
                if j == "T":
                    t = Teto()
                    t.rect.x = x
                    t.rect.y = y
                    self.sprite_ambiente.add(t)
                if j == "E":
                    e = Parede()
                    e.rect.x = x
                    e.rect.y = y
                    self.sprite_ambiente.add(e)
                if j == "P":
                    p = Porta()
                    p.rect.x = x
                    p.rect.y = y
                    self.sprite_porta.add(p)
                if j == "B":
                    b = Parede()
                    b.rect.x = x
                    b.rect.y = y
                    self.sprite_ambiente.add(b)
                if j == "S":
                    s = Solo()
                    s.rect.x = x
                    s.rect.y = y
                    self.sprite_ambiente.add(s)
                #if spritagem
                x += 32
            #for j
            y += 32
            x = 0
        #for i
    #nivel

    def esvaziar_sprites(self):
        self.sprite_ambiente.empty()
        self.sprite_porta.empty()
        self.sprite_inimigos.empty()
    #esvaziar_sprites

#Nivel