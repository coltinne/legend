#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from config import Config
#from game import Game


class Home:
    def __init__(self):
        try:
            reload(Game)
        except Exception:
            from game import *
        #except

        #Iniciando o pygame
        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(False)

        #Parametros do jogo
        self.config = Config("Home")
        self.mixer_music = pygame.mixer.music
        self.mixer_sound = pygame.mixer.Sound
        self.imagem = pygame.image
        self.clock = pygame.time.Clock()  #Criando o "relogio"
        self.musicas = self.config.musicas
        self.sons = self.config.sons

        #Menu
        self.menu = ["    Opcao    ", "    Iniciar    ", "    Sair    "]  #Valores do menu
        self.menu_som = self.config.musica_path + self.musicas[8]
        self.menu_backgroud = self.imagem.load(self.config.img_path + "bkmenu.png")
        self.menu_listac = ""  #Contrem o menu em si Controle
        self.menu_selecionado = 1  #A opcao selecionada
        self.menu_font = pygame.font.SysFont("verdana", 60)  #Fonte do menu
        self.menu_font_cor = [0, 0, 0]  #Cor da fonto do menu
        self.menu_centro = []  #Menu no centro
        self.som_slide = self.mixer_sound(self.config.som_path + self.sons[2])

        #Criando a tela
        self.tela = pygame.display.set_mode(self.config.tela, 0, 32)
        pygame.display.set_caption(self.config.tela_caption)

        #Largura do menu
        self.menu_largura()

        #Listagem dos menus
        self.menu_lista()

        #som de fundo do menu
        self.mixer_music.load(self.menu_som)
        self.mixer_music.play(-1)

        #Main loop
        while True:
            self.clock.tick(self.config.tick)
            for self.event in pygame.event.get():
                if self.event.type == QUIT:
                    exit()
                #if
                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_ESCAPE:
                        exit()
                    #if
                    if self.event.key == pygame.K_LEFT:
                        if self.menu_selecionado == 0:
                            self.menu_selecionado = len(self.menu) - 1
                            self.som_slide.play()
                        else:
                            self.menu_selecionado -= 1
                            self.som_slide.play()
                        #else
                    #if
                    if self.event.key == pygame.K_RIGHT:
                        if self.menu_selecionado == len(self.menu) - 1:
                            self.menu_selecionado = 0
                            self.som_slide.play()
                        else:
                            self.menu_selecionado += 1
                            self.som_slide.play()
                        #else
                    #if
                    if self.event.key == pygame.K_RETURN:
                        if self.menu_selecionado == 0:  #Opcoes
                            print "Config"
                        elif self.menu_selecionado == 1:    #iniciar
                            self.mixer_music.stop()
                            Game()
                        elif self.menu_selecionado == 2:    #Sair
                            exit()
                        #if
                    #if
                #if
            self.tela.fill(self.config.bgcolor)
            self.tela.blit(self.menu_backgroud, (0, 0))
            self.menu_controle()
            pygame.display.flip()
            #for
        #while
    #__init__

    def menu_largura(self):
        for i in self.menu:
            texto_surface = self.menu_font.render(i, True, self.menu_font_cor)
            self.menu_centro.append(texto_surface.get_width())
        #for
    #menu_largura

    def menu_lista(self):
        for i in self.menu:
            self.menu_listac += i
        #for
    #menu_lista

    def menu_controle(self):
        nmb = 0
        xpos = 0

        while nmb <= self.menu_selecionado:
            xpos -= self.menu_centro[nmb]
            nmb += 1
        #while

        xpos += self.menu_centro[self.menu_selecionado] / 2

        #escrever os menus
        texto_surface = self.menu_font.render(self.menu_listac, True, self.menu_font_cor)
        self.tela.blit(texto_surface, (400 + xpos, 500))
    #menu_controle

    def backgroud(self):
        pass
    #background
#Home

if __name__ == "__main__":
    Home()