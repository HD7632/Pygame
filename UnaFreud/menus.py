# se importa la libreria sobre la cual correrá el programa
import pygame
from levels import Objects
object = Objects()

#Clase del menu principal
class Pmenu:
    def __init__(self):
        #Defino sus botones
        self.stbt = pygame.Rect(140, 118, 24, 12)
        self.xtbt = pygame.Rect(140, 200, 24, 12)
    #Dibujo el menu
    def drawmenu(self, screen):
        #botones
        pygame.draw.rect(screen, (255, 0, 0), self.stbt)
        pygame.draw.rect(screen, (255, 0, 0), self.xtbt)

#Clase del menu de pausa
class Psmenu:
    def __init__(self):
        #Defino sus botones
        self.stbt = pygame.Rect(140, 118, 24, 12)
        self.xtbt = pygame.Rect(140, 200, 24, 12)

    #Dibujo el menu
    def drawpause(self, screen):
        #Botones
        pygame.draw.rect(screen, (0, 255, 0), self.stbt)
        pygame.draw.rect(screen, (0, 255, 0), self.xtbt)

#Clase del menu de muerte
class Dftmenu:
    def __init__(self):
        #Defino sus botones
        self.xtbt = pygame.Rect(140, 200, 24, 12)

    #Dibujo el menu
    def drawdefeat(self, screen):
        #Botones
        pygame.draw.rect(screen, (255, 0, 0), self.xtbt)