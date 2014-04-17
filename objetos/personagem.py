#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from sprites.spritesheet import SpriteSheet
from legend.config import Config


class Personagem(pygame.sprite.Sprite):
    def __init__(self, imagem, dimensao=(16, 32), sheet=False, local=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.config = Config()

        self.xvel = 0
        self.yvel = 0
        self.no_solo = True

        if sheet:
            self.sheet = SpriteSheet(imagem, dimensao)
            self.image = self.sheet.imagem_sheet[local[0]][local[1]]
            self.rect = self.image.get_rect()
        else:
            self.imagem = pygame.image.load(self.config.spr_path + imagem)  #Imagem do personagem
            self.sheet = SpriteSheet(imagem, dimensao)
            self.image = pygame.Surface(dimensao)
            self.image.fill(self.config.bgcolor)
            self.image.blit(self.imagem, (0, 0))
            self.rect = self.image.get_rect()
        #else
    #__init__
#Personagem
