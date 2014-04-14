#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import os, sys
from config import *
from objetos.parede import *
from objetos.solo import *
from objetos.porta import *


class Nivel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.config = Config()
        self.sprite_ambiente = pygame.sprite.Group()

        self.nivel = pygame.Surface(self.config.tela)
        self.nivel_marcador = 0

    #__init__

    def nivel_1(self):
        i = 0
        while i <= self.config.chao:
            parede = Parede()
            parede.rect = (0, i)
            self.sprite_ambiente.add(parede)
            if i == 192 or i == 384:
                x = 0
                while x <= 352:
                    parede = Parede()
                    parede.rect = (x, i)
                    x += 32
                    self.sprite_ambiente.add(parede)
                #while linha baixa
            #if
            if i == 96 or i == 288 or i == 480:
                x = 800
                while x >= 352:
                    parede = Parede()
                    parede.rect = (x, i)
                    x -= 32
                    self.sprite_ambiente.add(parede)
                #while linha baixa
            #if
            i += 32
        #while parede
        i = 0
        while i <= 800:
            solo = Solo()
            solo.rect = (i, self.config.chao)
            i += 32
            self.sprite_ambiente.add(solo)
        #while solo
        porta = Porta()
        porta.rect = (96, (537))
        self.sprite_ambiente.add(porta)
    #nivel_1
#Nivel