#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import os, sys
from config import *


class Personagem(pygame.sprite.Sprite):
    def __init__(self, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.config = Config()
        self.imagem = pygame.image.load(self.config.img_path + imagem)
        self.rect = self.imagem.get_rect()
    #__init__
#Personagem