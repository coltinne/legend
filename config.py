#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys


class Config:
    def __init__(self, caption = None):
        #Parametros do jogo
        self.tela = [800, 600]  #Tamanho da tela
        self.bgcolor = [198, 189, 172]  #Cor de fundo
        self.tela_caption = caption  #Titulo da Tela
        self.som_path = sys.path[0] + "/sons/"  #Path sons
        self.img_path = sys.path[0] + "/imagens/"   #Path imagens
        self.spr_path = sys.path[0] + "/sprites/"   #Path para Sprites

        #parametros da tela
        self.chao = 568

        #self.clock = pygame.time.Clock() #Criando o "relogio"
        self.tick = 60  #FPS
        #__init__
        #Config