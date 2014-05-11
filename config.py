#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys


class Config:
    def __init__(self, caption=None):
        #Parametros do jogo
        self.tela = [800, 600]  #Tamanho da tela
        #self.bgcolor = [198, 189, 172]  #Cor de fundo
        self.bgcolor = [10, 83, 114]  #Cor de fundo
        self.tela_caption = caption  #Titulo da Tela
        self.som_path = sys.path[0] + "/sons/"  #Path sons
        self.musica_path = sys.path[0] + "/musicas/"    #Path musicas
        self.img_path = sys.path[0] + "/imagens/"   #Path imagens
        self.spr_path = sys.path[0] + "/sprites/"   #Path para Sprites

        self.tick = 50  #FPS

        self.musicas = ["bangbang.ogg",
                        "darknightrain.ogg",
                        "electricquake.ogg",
                        "heartofmachine.ogg",
                        "perfecttime.ogg",
                        "rainbow.ogg",
                        "theorem.ogg",
                        "xu.ogg",
                        "zeta.ogg"]

        self.sons = ["chipquest.wav",
                     "jump.ogg",
                     "slide.ogg"]

    #__init__
#Config