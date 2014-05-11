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
        self.aberto = False
    #__init__

    def update(self, aberto):
        self.aberto = aberto
        if self.aberto:
            self.image = self.sheet.imagem_sheet[5][3]
        #if aberto
    #update
#Porta


class Solo(Objetos):
    def __init__(self):
        Objetos.__init__(self, "telaobjetos.png", (1, 0))
    #__init__
#Solo


class Teto(Objetos):
    def __init__(self):
        Objetos.__init__(self, "telaobjetos.png", (6, 6))
    #__init__
#Teto


class Chave(Objetos):
    def __init__(self):
        Objetos.__init__(self, "telaobjetos.png", (4, 4))
    #__init__
#Chave


class Fogo(Objetos):
    def __init__(self):
        Objetos.__init__(self, "telaobjetos.png", (4, 1))
    #__init__
#Fogo


class Clunk(Objetos):
    def __init__(self):
        Objetos.__init__(self, "telaobjetos.png", (7, 2))
        self.xvel = 6
    #__innit__

    def update(self):
        self.rect.x += self.xvel
    #update
#Clunk


class Plataforma(Objetos):
    def __init__(self):
        Objetos.__init__(self, "telaobjetos.png", (0, 6))
        self.xvel = 2
    #__init__

    def update(self):
        self.rect.x += self.xvel
    #update
#Plataforma


class Agua(Objetos):
    def __init__(self):
        Objetos.__init__(self, "telaobjetos.png", (3, 1))
    #__init__
#Agua


class Elevador(Objetos):
    def __init__(self):
        Objetos.__init__(self, "telaobjetos.png", (3, 2))
        self.xvel = 2
    #__innit__

    def update(self):
        self.rect.x += self.xvel
    #update
#Elevador


class Nuvem(Objetos):
    def __init__(self):
        Objetos.__init__(self, "telaobjetos.png", (6, 3))
        self.xvel = 4
    #__init__

    def update(self):
        self.rect.x += self.xvel
    #update
#Nuvem