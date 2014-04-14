#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from config import *


class SpriteSheet():
    def __init__(self, imagem, dimensao=None, listar=False):
        self.rect = [[0 for i in range(100)] for j in range(100)]
        self.config = Config()
        self.sheet = pygame.image.load(self.config.spr_path + imagem)
        self.imagem_sheet = [[0 for i in range(100)] for j in range(100)]
        if listar:
            self.imagem_array(dimensao)
        #listar
    #__init__

    def imagem_mapa(self, posicao):
        rect = pygame.Rect(posicao)
        imagem = pygame.Surface(rect.size)
        imagem.fill([0, 0, 0])
        imagem.blit(self.sheet, (0, 0), rect)
        return imagem
    #image_map

    def imagem_array(self, dimemsao):
        xpos = self.sheet.get_size()[0]
        ypos = self.sheet.get_size()[1]
        indice_x = dimemsao[0]
        indice_y = dimemsao[1]
        quantidade_objeto_x = xpos / indice_x
        quantidade_objeto_y = ypos / indice_y
        xpos = 0
        ypos = 0
        for x in range(0, quantidade_objeto_x):
            for y in range(0, quantidade_objeto_y):
                self.imagem_sheet[x][y] = self.imagem_mapa((xpos, ypos, indice_x, indice_y))
                ypos += 32
            #for j
            ypos = 0
            xpos += 32
        #for i
    #imagem_lista