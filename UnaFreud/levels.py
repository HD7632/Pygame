# se importa la libreria sobre la cual correrá el programa
import pygame
class Objects:
    def __init__(self):
        #Defino el ancho y alto de la pantalla
        self.width = 304
        self.height = 224
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.floor = 135

        #Fondo
        self.bkgr_1 = pygame.image.load("Pygame/UnaFreud/Assets/Background/Background_0.png").convert();
        
        #Defino una variable que servirá para controlar los fps
        self.clock = pygame.time.Clock()