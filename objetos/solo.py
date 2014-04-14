#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from legend.spritesheet import *


class Solo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dimensao = (32, 32)
        self.config = Config()
        self.sheet = SpriteSheet("telaobjetos.png", self.dimensao, True)

        #objeto
        self.image = self.sheet.imagem_sheet[1][0]
        self.rect = self.image.get_rect()
    #__init__
#Solo