#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from home import Home
from config import Config
from nivel import Nivel
from objetos.personagem import Personagem

#Controla a açao da porta
go = False
abrir = False

#Controle de Niveis
nivel = Nivel()
ambiente = nivel.sprite_ambiente
inimigos = nivel.sprite_inimigos
portal = nivel.sprite_porta
chave = nivel.sprite_chave
armadilha = nivel.sprite_armadilha
respawn = nivel.respawn
monstro = nivel.sprite_monstro
plataforma = nivel.sprite_plataforma
agua = nivel.sprite_agua
elevador = nivel.sprite_elevador
nuvem = nivel.sprite_nuvem


class Game:
    def __init__(self):
        global go, abrir, nivel

        if not pygame.init():
            pygame.init()
        if not pygame.font.init():
            pygame.font.init()

        #configuraçoes
        self.config = Config("Game")
        self.clock = pygame.time.Clock()
        self.imagem = pygame.image
        self.musicas = self.config.musicas
        self.sons = self.config.sons
        self.mixer_music = pygame.mixer.music
        self.mixer_sound = pygame.mixer.Sound

        #Menu
        self.menu = ["Reiniciar Fase", "Menu Principal", "Configuracoes", "Salvar", "Sair"]
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

        #sons do jogo
        self.som_slide = self.mixer_sound(self.config.som_path + self.sons[2])
        self.som_pulo = self.mixer_sound(self.config.som_path + self.sons[1])

        #Controle dos menus
        self.left = self.right = self.up = self.down = self.run = self.no_solo = False

        #Player
        self.player = Player()
        self.player.rect.x = 500
        self.player.rect.y = 540
        self.g_player = pygame.sprite.Group()
        self.g_player.add(self.player)

        #tocar musicas das fases
        nivel.musica()

        while True:

            self.clock.tick(self.config.tick)

            go = False

            for self.event in pygame.event.get():
                if self.event.type == QUIT:
                    exit()
                if self.event.type == KEYDOWN:
                    if self.event.key == pygame.K_ESCAPE:
                        self.menu_exibir()
                    if self.event.key == pygame.K_RETURN:
                        print "ok"

                if self.event.type == KEYDOWN and self.event.key == K_LEFT:
                    self.left = True
                if self.event.type == KEYDOWN and self.event.key == K_RIGHT:
                    self.right = True
                if self.event.type == KEYDOWN and self.event.key == K_z:
                    self.up = True
                    self.som_pulo.play()
                if self.event.type == KEYDOWN and self.event.key == K_DOWN:
                    self.down = True
                if self.event.type == KEYDOWN and self.event.key == K_x:
                    self.run = True
                if self.event.type == KEYDOWN and self.event.key == K_UP:
                    go = True

                if self.event.type == KEYUP and self.event.key == K_LEFT:
                    self.left = False
                if self.event.type == KEYUP and self.event.key == K_RIGHT:
                    self.right = False
                if self.event.type == KEYUP and self.event.key == K_z:
                    self.up = False
                if self.event.type == KEYUP and self.event.key == K_DOWN:
                    self.down = False
                if self.event.type == KEYUP and self.event.key == K_x:
                    self.run = False
                if self.event.type == KEYDOWN and self.event.key == K_UP:
                    pass
            #for pygame event

            self.tela.fill(self.config.bgcolor)

            ambiente.update()
            ambiente.draw(self.tela)

            portal.update(abrir)
            portal.draw(self.tela)

            armadilha.update()
            armadilha.draw(self.tela)

            elevador.update()
            elevador.draw(self.tela)

            colisao_movimento()

            monstro.update()
            monstro.draw(self.tela)

            plataforma.update()
            plataforma.draw(self.tela)

            nuvem.update()
            nuvem.draw(self.tela)

            agua.draw(self.tela)

            self.g_player.update(self.left, self.right, self.up, self.down, self.run)
            self.g_player.draw(self.tela)

            chave.update()
            chave.draw(self.tela)

            pygame.display.flip()
        #while main loop
    #__init__

    def loadscr(self):
        self.tela.blit(self.imagem.load(self.config.img_path + "loadingscreen.png"), (0, 0))
    #loadscr

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
            #if menu selecionado
            self.tela.blit(texto_surface, (400 - xpos, 200 - ypos + y2pos))
            cont += 1
        #for
    #menu_controle

    def menu_exibir(self):
        global abrir
        var = True
        while var:  #Eventos do menu
            for self.eventm in pygame.event.get():
                if self.eventm.type == QUIT:
                    exit()
                if self.eventm.type == pygame.KEYDOWN:
                    if self.eventm.key == pygame.K_ESCAPE:
                        self.menu_selecionado = 0
                        var = False
                    #if key esc
                    if self.eventm.key == pygame.K_DOWN:
                        if self.menu_selecionado == 0:
                            #self.menu_selecionado = len(self.menu) - 1
                            self.som_slide.play()
                        else:
                            self.menu_selecionado -= 1
                            self.som_slide.play()
                    #if key down
                    if self.eventm.key == pygame.K_UP:
                        if self.menu_selecionado == len(self.menu) - 1:
                            #self.menu_selecionado = 0
                            self.som_slide.play()
                        else:
                            self.menu_selecionado += 1
                            self.som_slide.play()
                    #if key up
                    if self.eventm.key == pygame.K_RETURN:
                        if self.menu_selecionado == 0:  #Reiniciar fase
                            self.player.rect.x = respawn[0]
                            self.player.rect.y = respawn[1]
                            abrir = False
                            var = False
                        if self.menu_selecionado == 1:  #Tela inicial
                            nivel.zerar()
                            Home()
                        elif self.menu_selecionado == 2:    #Configuracoes
                            print "Config"
                        elif self.menu_selecionado == 3:    #Salvar
                            print "Saltar"
                        elif self.menu_selecionado == 4:    #Sair
                            exit()
                #if key down
            #for pygame get event

            self.tela.fill(self.config.bgcolor)
            self.menu_controle()
            pygame.display.flip()
        #while main loo
    #menu_exibir
#Game


class Player(Personagem):
    def __init__(self):
        Personagem.__init__(self, "imp.png")
    #__init__

    def update(self, left=False, right=False, up=False, down=False, run=False):
        if left:
            self.xvel = -5
        if right:
            self.xvel = 5
        if up and self.no_solo:
            self.yvel = -5
        if down and not self.no_solo:
            self.yvel = 6
        if run:
            if self.xvel > 0:
                self.xvel = 7
            else:
                self.xvel = -7
            if up and self.no_solo:
                self.yvel = -8
        #if movimentos

        if not self.no_solo:
            self.yvel += 0.3
            if self.yvel > 100:
                self.yvel = 100
        #if gravidade

        if not (left or right):
            self.xvel = 0

        if not up and self.no_solo:
            self.yvel = 0

        self.rect.x += self.xvel
        colisao(self, self.xvel, 0)

        self.rect.y += self.yvel
        self.no_solo = False
        colisao(self, 0, self.yvel)
    #update
#Plyer


def colisao(objeto, xvel, yvel):
    global abrir, respawn
    local = ambiente
    for i in local:
        if pygame.sprite.collide_rect(objeto, i):
            if xvel > 0:
                objeto.rect.right = i.rect.left
            if xvel < 0:
                objeto.rect.left = i.rect.right
            if yvel > 0:
                objeto.rect.bottom = i.rect.top
                objeto.no_solo = True
                objeto.yvel = 0
            if yvel < 0:
                objeto.rect.top = i.rect.bottom
    #ambiente
    local = plataforma
    for i in local:
        if pygame.sprite.collide_rect(objeto, i):
            if xvel > 0:
                objeto.rect.right = i.rect.left
            if xvel < 0:
                objeto.rect.left = i.rect.right
            if yvel > 0:
                objeto.rect.bottom = i.rect.top
                objeto.no_solo = True
                objeto.yvel = 0
            if yvel < 0:
                objeto.rect.top = i.rect.bottom
    #plataforma

    local = portal
    for i in local:
        if pygame.sprite.collide_rect(objeto, i):
            if go and abrir:
                nivel.next_nivel()
                respawn = nivel.respawn
                abrir = False
    #portal

    local = chave
    for i in local:
        if pygame.sprite.collide_rect(objeto, i):
            if go:
                abrir = True
    #chave

    local = armadilha
    for i in local:
        if pygame.sprite.collide_rect(objeto, i):
            objeto.rect.x = respawn[0]
            objeto.rect.y = respawn[1]
    #armadilha

    local = monstro
    for i in local:
        if pygame.sprite.collide_rect(objeto, i):
            objeto.rect.x = respawn[0]
            objeto.rect.y = respawn[1]
    #monstro

    local = agua
    for i in local:
        if pygame.sprite.collide_rect(objeto, i):
            objeto.rect.y -= 10
    #agua

    local = elevador
    for i in local:
        if pygame.sprite.collide_rect(objeto, i):
            objeto.rect.x = i.rect.x
            objeto.rect.y = i.rect.y
            objeto.rect.center = i.rect.center
            objeto.no_solo = True
            if go:
                objeto.rect.y += 32
    #elevador

    local = nuvem
    for i in local:
        if pygame.sprite.collide_rect(objeto, i):
            objeto.rect.x = i.rect.x
            objeto.rect.center = i.rect.center
            objeto.no_solo = True
            if go:
                objeto.rect.y -= 64
    #nuvem
#colisao


def colisao_movimento():
    local = ambiente
    objeto = monstro
    for i in objeto:
        if pygame.sprite.spritecollideany(i, local):
            for j in local:
                if pygame.sprite.collide_rect(i, j):
                    if i.xvel > 0:
                        i.xvel = -6
                    else:
                        i.xvel = 6
    #monstro

    objeto = plataforma
    for i in objeto:
        if pygame.sprite.spritecollideany(i, local):
            for j in local:
                if pygame.sprite.collide_rect(i, j):
                    if i.xvel > 0:
                        i.xvel = -2
                    else:
                        i.xvel = 2
    #plataforma

    objeto = elevador
    for i in objeto:
        if pygame.sprite.spritecollideany(i, local):
            for j in local:
                if pygame.sprite.collide_rect(i, j):
                    if i.xvel > 0:
                        i.xvel = -2
                    else:
                        i.xvel = 2
    #elevador

    objeto = nuvem
    for i in objeto:
        if pygame.sprite.spritecollideany(i, local):
            for j in local:
                if pygame.sprite.collide_rect(i, j):
                    if i.xvel > 0:
                        i.xvel = -4
                    else:
                        i.xvel = 4
    #nuvem
#colisao_monstro

if __name__ == "__main__":
    Game()