#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from sprites.spritesheet import SpriteSheet
from legend.config import Config


class Personagem(pygame.sprite.Sprite):
    def __init__(self, imagem, dimensao=(16, 32), sheet=False, local=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.config = Config()

        if sheet:
            self.sheet = SpriteSheet(imagem, dimensao)
            self.image = self.sheet.imagem_sheet[local[0]][local[1]]
            self.rect = self.image.get_rect()
        else:
            self.imagem = pygame.image.load(self.config.spr_path + imagem).convert()  #Imagem do personagem
            self.sheet = SpriteSheet(imagem, dimensao)
            self.image = pygame.Surface(dimensao)
            self.image.blit(self.imagem, (0, 0))
            self.rect = self.image.get_rect()
        #else
    #__init__

    def update(self):
        if False:
            pass
        else:
            self.rect.y += 5
    #update

    def mover_esquerda(self):
        self.rect.x -= 10
    #mover_esquerda

    def mover_direita(self):
        self.rect.x += 10
    #mover_esquerda

    def mover_pular(self):
        self.rect.y -= 1
    #mover_pular

    def mover_baixo(self):
        self.rect.y += 10
    #mover_baixo
#Personagem


class Imp(Personagem):
    def __init__(self):
        Personagem.__init__(self, "imp.png")
    #__init__
#Imp