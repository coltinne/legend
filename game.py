#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import os, sys
from home import *
from config import *
from nivel import *


class Game:
    def __init__(self):
        if not pygame.init():
            pygame.init()
        if not pygame.font.init():
            pygame.font.init()
        #if

        #configuraçoes
        self.config = Config("Game")
        self.clock = pygame.time.Clock()
        self.imagem = pygame.image

        self.nivel = Nivel()

        #Menu
        self.menu = ["Menu Principal", "Configuracoes", "Salvar", "Sair"]
        self.menu_font_size = 30
        self.menu_font = pygame.font.SysFont("arial", self.menu_font_size)
        self.menu_font_cor = [0, 0, 0]
        self.menu_listac = ""
        self.menu_selecionado = 0
        self.menu_centro = []
        self.menu_imagem = self.imagem.load(self.config.img_path + "menuplay.png")

        #criar tela
        self.tela = pygame.display.set_mode(self.config.tela, 0, 32)
        pygame.display.set_caption(self.config.tela_caption)

        #calculando centro
        self.menu_largura()

        #listar o menu
        #self.menu_lista()

        #som de transicao do menu
        self.som_slide = pygame.mixer.Sound(self.config.som_path + "slide.ogg")

        #Gerar sprites
        #self.nivel.nivel_1()
        self.chao = self.nivel.nivel_1()

        while True:
            self.clock.tick(self.config.tick)
            for self.event in pygame.event.get():
                if self.event.type == QUIT:
                    exit()
                #if
                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_ESCAPE:
                        self.menu_exibir()
                    #if
                    if self.event.key == pygame.K_RETURN:
                        print "ok"
                    #if
                #if

                self.nivel.sprite_ambiente.update()
                self.nivel.sprite_ambiente.draw(self.tela)
                pygame.display.flip()
                #if
            #for
        #while
    #__init__

    def menu_largura(self):
        for i in self.menu:
            texto_surface = self.menu_font.render(i, True, self.menu_font_cor)
            self.menu_centro.append(texto_surface.get_width())
        #for
    #menu_largura

    def menu_controle(self):
        y2pos = 0
        cont = 0
        self.tela.blit(self.menu_imagem, (0, 0))
        for i in self.menu:
            self.menu_listac = i
            texto_surface = self.menu_font.render(self.menu_listac, True, self.menu_font_cor)
            y2pos += self.menu_font_size
            xpos = self.menu_centro[cont] / 2
            if self.menu_selecionado == 0:
                ypos = self.menu_font_size
            else:
                ypos = self.menu_font_size * (self.menu_selecionado + 1)
            #else
            self.tela.blit(texto_surface, (400 - xpos, 200 - ypos + y2pos))
            cont += 1
        #for
    #menu_controle

    def menu_exibir(self):
        var = True
        while var:  #Eventos do menu
            for self.eventm in pygame.event.get():
                if self.eventm.type == QUIT:
                    exit()
                #if
                if self.eventm.type == pygame.KEYDOWN:
                    if self.eventm.key == pygame.K_ESCAPE:
                        self.menu_selecionado = 0
                        var = False
                    #if
                    if self.eventm.key == pygame.K_DOWN:
                        if self.menu_selecionado == 0:
                            #self.menu_selecionado = len(self.menu) - 1
                            self.som_slide.play()
                        else:
                            self.menu_selecionado -= 1
                            self.som_slide.play()
                        #else
                    #if
                    if self.eventm.key == pygame.K_UP:
                        if self.menu_selecionado == len(self.menu) - 1:
                            #self.menu_selecionado = 0
                            self.som_slide.play()
                        else:
                            self.menu_selecionado += 1
                            self.som_slide.play()
                        #else
                    #if
                    if self.eventm.key == pygame.K_RETURN:
                        if self.menu_selecionado == 0:  #Tela inicial
                            Home()
                        elif self.menu_selecionado == 1:    #Configuracoes
                            print "Config"
                        elif self.menu_selecionado == 2:    #Salvar
                            print "Saltar"
                        elif self.menu_selecionado == 3:    #Sair
                            exit()
                        #elif
                    #if
                #if
            #for
            self.tela.fill(self.config.bgcolor)
            self.menu_controle()
            pygame.display.flip()
        #while
    #menu_exibir
#Game

if __name__ == "__main__":
    Game()