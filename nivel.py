#!/usr/bin/env python
#-*- coding: utf-8 -*-

from objetos.parede import *
from objetos.solo import *
from objetos.porta import *
from objetos.personagem import *
from objetos.imp import *


class Nivel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.config = Config()
        self.sprite_ambiente = pygame.sprite.Group()
        self.sprite_inimigos = pygame.sprite.Group()

        self.imp = Imp()

        self.nivel = pygame.Surface(self.config.tela)
        self.nivel_marcador = 0

    #__init__

    def nivel_1(self):
        i = 0
        while i <= self.config.chao:
            parede = Parede()
            parede.rect.x = 0
            parede.rect.y = i
            self.sprite_ambiente.add(parede)
            if i == 192 or i == 384:
                x = 0
                while x <= 352:
                    parede = Parede()
                    parede.rect.x = x
                    parede.rect.y = i
                    x += 32
                    self.sprite_ambiente.add(parede)
                #while linha baixa
            #if
            if i == 96 or i == 288 or i == 480:
                x = 800
                while x >= 352:
                    parede = Parede()
                    parede.rect.x = x
                    parede.rect.y = i
                    x -= 32
                    self.sprite_ambiente.add(parede)
                #while linha baixa
            #if
            i += 32
        #while parede
        i = 0
        while i <= 800:
            solo = Solo()
            solo.rect.x = i
            solo.rect.y = self.config.chao
            i += 32
            self.sprite_ambiente.add(solo)
        #while solo

        porta = Porta()
        porta.rect.x = 96
        porta.rect.y = 537
        self.sprite_ambiente.add(porta)

        self.imp.rect.x = 225
        self.imp.rect.y = 250
        self.sprite_inimigos.add(self.imp)
    #nivel_1
#Nivel