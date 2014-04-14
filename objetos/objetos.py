#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame

from legend.config import Config
from sprites.spritesheet import SpriteSheet


class Objetos(pygame.sprite.Sprite):
    def __init__(self, sheet, vetor):
        pygame.sprite.Sprite.__init__(self)
        self.dimensao = (32, 32)
        self.config = Config()
        self.sheet = SpriteSheet(sheet, self.dimensao, True)

        #objeto
        self.image = self.sheet.imagem_sheet[vetor[0]][vetor[1]]
        self.rect = self.image.get_rect()
    #__init__
#Objetos


class Parede(Objetos):
    def __init__(self):
        Objetos.__init__(self, "telaobjetos.png", (0, 3))
    #__init__
#Parede


class Porta(Objetos):
    def __init__(self):
        Objetos.__init__(self, "telaobjetos.png", (4, 3))
    #__init__
#Porta


class Solo(Objetos):
    def __init__(self):
        Objetos.__init__(self, "telaobjetos.png", (1, 0))
    #__init__
#Solo