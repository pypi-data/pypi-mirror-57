import random
import pygame
import sys
import os
from pygame.locals import *
from Resources.sprites.sprite import Sprite
class BackGround(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        n=2
        self.element.append(pygame.image.load(Get('bg_' + str(n) + '.png')))
    def GetEement(self):
        return self.element[0]

def Get(name):
    return os.path.dirname(os.path.realpath(__file__))+"\\"+name



