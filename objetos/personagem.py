#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
import legend
from legend.spritesheet import *
from legend.config import *


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
        if self.rect.y > 530:
            pass
        else:
            self.rect.y += 5
    #update

    def mover_esquerda(self):
        if self.rect.x <= 0:
            pass
        else:
            self.rect.x -= 10
        #else
    #mover_esquerda

    def mover_direita(self):
        if self.rect.x > self.config.tela[0] - 16:
            pass
        else:
            self.rect.x += 10
        #else
    #mover_esquerda

    def mover_pular(self):
        for i in range(0, 65):
            pygame.time.wait(1)
            self.rect.y -= 1
    #mover_pular

    def mover_baixo(self):
        self.rect.y += 10
#Personagem