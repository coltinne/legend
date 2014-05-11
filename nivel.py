#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from config import Config
from objetos.objetos import *
from objetos.personagem import *


class Nivel():
    def __init__(self):
        self.config = Config()
        self.sprite_ambiente = pygame.sprite.Group()    #T(teto) E,B(parede) S(solo)
        self.sprite_porta = pygame.sprite.Group()   #P(porta)
        self.sprite_chave = pygame.sprite.Group()   #C(chave)
        self.sprite_inimigos = pygame.sprite.Group()    #Nao usado
        self.sprite_armadilha = pygame.sprite.Group()   #F(fogo)
        self.sprite_monstro = pygame.sprite.Group()    #K(Clunk)
        self.sprite_plataforma = pygame.sprite.Group()    #A(plataforma)
        self.sprite_agua = pygame.sprite.Group()    #G(agua)
        self.sprite_elevador = pygame.sprite.Group()    #V(elevador)
        self.sprite_nuvem = pygame.sprite.Group()    #N(nuvem)

        self.fase = 8
        self.level = []
        self.respawn = 0

        self.level_modelo()
        self.nivel()
    #__init__

    def level_modelo(self):
        if self.fase == 0:
            self.level = [
                "TTTTTTTTTTTTTTTTTTTTTTTTT",
                "E-----------------------E",
                "E--------------------P--E",
                "E-------------------BBBBE",
                "E-------------BBBBBBB---E",
                "E-------BBBBBBB---------E",
                "EBB---------------------E",
                "E--BBB------------------E",
                "E--C--BBBBB-------------E",
                "E-BBBB------------------E",
                "E-------------BBBBBBBB--E",
                "EBBBBBBBB---------------E",
                "E-----------------------E",
                "E-----------BBBBBB------E",
                "EBBBBBB-----------------E",
                "E-----------------------E",
                "E------BBBBBB-----------E",
                "E-----------------------E",
                "ESSSSSSSSSSSSSSSSSSSSSSSE", ]
        elif self.fase == 1:
            self.level = [
                "TTTTTTTTTTTTTTTTTTTTTTTTT",
                "E-------P-----B---------E",
                "E--B-BBBBBBB--B-B-------E",
                "E-B--B-BB-----B------R--E",
                "E-K-------BBBBBBBBBBBB--E",
                "E-BBBBBBB--B---BB----BB-E",
                "E----------------B------E",
                "E----------BB---BBB--BBBE",
                "EBBBBBBBBBBB--B-B-BB----E",
                "E-------------BB--BBBBB-E",
                "E-B-BBBBBBBBBBBBBBB-----E",
                "E-----------------B-B---E",
                "EBBBBBBBBBB-B-BBBB---BBBE",
                "E---------B---B-B-------E",
                "EBBBBBBBB---BBBBBBBBBB-BE",
                "EC-----------------B----E",
                "EB-----BBB----B---------E",
                "E------K------BBBBBBBBBBE",
                "ESSSSSSSSSSSSSSSSSSSSSSSE", ]
        elif self.fase == 2:
            self.level = [
                "TTTTTTTTTTTTTTTTTTTTTTTTT",
                "E-------R---------------E",
                "E-K----BBB------------K-E",
                "E-K---------------------E",
                "E---------------------K-E",
                "E-----------------------E",
                "E-----------------------E",
                "E-K---------------------E",
                "E------------------C----E",
                "E-K---------------SS----E",
                "E---------------------K-E",
                "E-K---------------------E",
                "E---------------------K-E",
                "E-----------------------E",
                "E-----------------------E",
                "E-K---------------------E",
                "E-P-------------------K-E",
                "E-S---------------------E",
                "EFFFFFFFFFFFFFFFFFFFFFFFE", ]

        elif self.fase == 3:
            self.level = [
                "TTTTTTTTTTTTTTTTTTTTTTTTT",
                "EC----------------------E",
                "EE--------------AA------E",
                "E-----------------------E",
                "E-----------------------E",
                "E---AA------------------E",
                "E-----------------------E",
                "E----------------AA-----E",
                "E-----------------------E",
                "E--AA-------------------E",
                "E-----------------------E",
                "E----------------AA-----E",
                "E-----------------------E",
                "E--AA-------------------E",
                "E-----------------------E",
                "E-------------AA--------E",
                "E-R---------------------E",
                "E----------------------PE",
                "ESSSSSSSSSSSSSSSSSSSSSSSE", ]

        elif self.fase == 4:
            self.level = [
                "TTTTTTTTTTTTTTTTTTTTTTTTT",
                "E-----------------------E",
                "E-F----S----------------E",
                "E-F---------------------E",
                "E-F----------S----------E",
                "E-F---------------------E",
                "E-F------S--------------E",
                "E-F---------------------E",
                "E-FA-A-A-A-A-A-A-A-A-A-AE",
                "E-F---------------------E",
                "E-F----------SSS-------CE",
                "E-FK-------------------EE",
                "E-F--------------A-A----E",
                "E-F---------------------E",
                "E-FSSS------------------E",
                "E-F--------K------------E",
                "E-F--------AA-----------E",
                "EPF--------------------RE",
                "ESSSSSSSSSSSSSSSSSSSSSSSE", ]

        elif self.fase == 5:
            self.level = [
                "TTTTTTTTTTTTTTTTTTTTTTTTT",
                "E-----------------------E",
                "E--F--FFFSSFFFFSSFFFFS--E",
                "E--F--F------K--------SGE",
                "E--F--F----------------GE",
                "E--F--F---------FFFFF--GE",
                "E--F--F-----K--F-----F-GE",
                "E--F--F-------F------F-GE",
                "E--F--F------F-------F-GE",
                "E--F--F--------------F-GE",
                "E--FP-FFFFF--K-FFF-----GE",
                "E--FSS------SS-----SS---E",
                "E----------------------CE",
                "E---------------K------SE",
                "E---------SS------------E",
                "EK----------------------E",
                "E----SS-----------------E",
                "ER----------------------E",
                "ESSSSSSSSSSSSSSSSSSSSSSSE", ]

        elif self.fase == 6:
            self.level = [
                "TTTTTTTTTTTTTTTTTTTTTTTTT",
                "EP----------------------E",
                "ES--------AAAA----------E",
                "EK----------------------E",
                "E---------SSSS-----F----E",
                "E----------K------------E",
                "EK-A-S-F---A--F---A-S--KE",
                "E-KF---A--F----A--F--AK-E",
                "ESAK-------AF-----A-FK-SE",
                "E--FK-A--A-S-A---AF-K---E",
                "E-A--K-F---A--F-A--KA-F-E",
                "E---R-------------------E",
                "ES-A-A-A-A-A-A-A-A-A-SSSE",
                "ESS-A-A-A-ACA-A-A-A-A-SSE",
                "ESSS-A-A-A-A-A-A-A-A-A-SE",
                "E-----------------------E",
                "E-----------------------E",
                "EAAAAAAAAAAAAAAAAAAAAAAAE",
                "ESSSSSSSSSSSSSSSSSSSSSSSE", ]

        elif self.fase == 7:
            self.level = [
                "TTTTTTTTTTTTTTTTTTTTTTTTT",
                "ER---------------------CE",
                "ES-------A-------A-----SE",
                "EFFFFF00F0K0F0FFF000FFFFE",
                "EFFFFF0FF0F0FKFFFF0FFFFFE",
                "EFFFFFK0F000F000FF0FFFFFE",
                "E-----------------------E",
                "E----------------------VE",
                "E-----------------------E",
                "EFFFFFFFKFFFFFFFFFFFFFFFE",
                "EFFFFFFFKFFFFFFFFFFFFFFFE",
                "EFFFFFFFKFFFFFFFFFFFFFFFE",
                "E-----------------------E",
                "EV----------------------E",
                "E-------E---------------E",
                "EFFFF00FF0F00FF0F00KFFFFE",
                "EFFFF0F0F0F0FKF0F00FFFFFE",
                "EFFFFKFF00F0FF00F0P0FFFFE",
                "ESSSSSSSSSSSSSSSSSSSSSSSE", ]

        elif self.fase == 8:
            self.level = [
                "TTTTTTTTTTTTTTTTTTTTTTTTT",
                "E-----K-----------K----PE",
                "E------------------A----E",
                "E---A-------------------E",
                "E---------------A-------E",
                "E----------C------------E",
                "E-F-FAF-F-F-FAF-F-FAF-FGE",
                "E----K-----------------GE",
                "E----------K-----------GE",
                "E----------------------GE",
                "E-FBFBFBFBFBFBFBFBFBFBFBE",
                "EG---------------K------E",
                "EG-----K----------------E",
                "EG-----S----N-----------E",
                "EGK----FFFFFF--FF-F-F-F-E",
                "EG-----F-------F-------KE",
                "EG-----F-K-----F--------E",
                "E--------------F--R-----E",
                "ESSSSSSSSSSSSSSSSSSSSSSSE", ]

        elif self.fase == 9:
            self.level = [
                "TTTTTTTTTTTTTTTTTTTTTTTTT",
                "E-----------------------E",
                "E-----------------------E",
                "E-----------------------E",
                "E-----------------------E",
                "E-----------------------E",
                "E-----------------------E",
                "E-----------------------E",
                "E-----------------------E",
                "E-----------------------E",
                "E-----------------------E",
                "E-----------------------E",
                "E-----------------------E",
                "E---------------------V-E",
                "E-----------------------E",
                "E----------N-----------BE",
                "E---------------------BBE",
                "E-----------------------E",
                "ESSSSSSSSSSSSSSSSSSSSSSSE", ]
    #level

    def next_nivel(self):
        self.fase += 1
        self.esvaziar_sprites()
        self.level_modelo()
        self.nivel()
    #next nivel

    def prev_nivel(self):
        self.fase -= 1
        self.esvaziar_sprites()
        self.level_modelo()
        self.nivel()
    #prev nivel

    def nivel(self):
        x = y = 0
        for i in self.level:
            for j in i:
                if j == "T":
                    t = Teto()
                    t.rect.x = x
                    t.rect.y = y
                    self.sprite_ambiente.add(t)
                if j == "E":
                    e = Parede()
                    e.rect.x = x
                    e.rect.y = y
                    self.sprite_ambiente.add(e)
                if j == "P":
                    p = Porta()
                    p.rect.x = x
                    p.rect.y = y
                    self.sprite_porta.add(p)
                if j == "B":
                    b = Parede()
                    b.rect.x = x
                    b.rect.y = y
                    self.sprite_ambiente.add(b)
                if j == "S":
                    s = Solo()
                    s.rect.x = x
                    s.rect.y = y
                    self.sprite_ambiente.add(s)
                if j == "C":
                    c = Chave()
                    c.rect.x = x
                    c.rect.y = y
                    self.sprite_chave.add(c)
                if j == "F":
                    f = Fogo()
                    f.rect.x = x
                    f.rect.y = y
                    self.sprite_armadilha.add(f)
                if j == "R":
                    self.respawn = (x, y)
                if j == "K":
                    k = Clunk()
                    k.rect.x = x
                    k.rect.y = y
                    self.sprite_monstro.add(k)
                if j == "A":
                    a = Plataforma()
                    a.rect.x = x
                    a.rect.y = y
                    self.sprite_plataforma.add(a)
                if j == "G":
                    g = Agua()
                    g.rect.x = x
                    g.rect.y = y
                    self.sprite_agua.add(g)
                if j == "V":
                    v = Elevador()
                    v.rect.x = x
                    v.rect.y = y
                    self.sprite_elevador.add(v)
                if j == "N":
                    n = Nuvem()
                    n.rect.x = x
                    n.rect.y = y
                    self.sprite_nuvem.add(n)
                #if spritagem
                x += 32
            #for j
            y += 32
            x = 0
        #for i
    #nivel

    def esvaziar_sprites(self):
        self.sprite_ambiente.empty()
        self.sprite_porta.empty()
        self.sprite_inimigos.empty()
        self.sprite_chave.empty()
        self.sprite_armadilha.empty()
        self.sprite_monstro.empty()
        self.sprite_plataforma.empty()
        self.sprite_agua.empty()
        self.sprite_elevador.empty()
        self.sprite_nuvem.empty()
    #esvaziar_sprites

    def zerar(self):
        self.fase = 0
        self.esvaziar_sprites()
        self.level_modelo()
        self.nivel()

#Nivel