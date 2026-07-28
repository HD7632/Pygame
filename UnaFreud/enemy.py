# se importa la libreria sobre la cual correrá el programa
import pygame
from levels import Objects
from gasbombs import Gasbomb

object = Objects()
class Truck:
    def __init__(self):
        self.v = [-38, 0]
        self.pos = [267.5, 140]
        self.hitbox = pygame.Rect(225, 95, 65, 45)
        self.hitbox.size = (65, 45)
        self.hitbox.midbottom = self.pos
        self.state = 'moving'
        self.direction = 'left'
        self.shooter1dt = 0
        self.shooter2dt = 0

        self.img_pos = [0, 93]
        self.gasbombs = []

        #Jugador
        self.img = pygame.image.load("Pygame/UnaFreud/Assets/Enemy/Truck_Left.png").convert_alpha()
        

        #IMAGENES
        self.Sprites = {
            "moving_right": pygame.image.load("Pygame/UnaFreud/Assets/Enemy/Truck_Right.png").convert_alpha(),

            "moving_left":pygame.image.load("Pygame/UnaFreud/Assets/Enemy/Truck_Left.png").convert_alpha(),
        }  

    def mvnt(self,dt):
        self.pos[0] = self.pos[0]+self.v[0]*dt

        if self.pos[0] < 200:
            self.v[0] = 38
            self.direction = 'right'
        if self.pos[0] > 267:
            self.v[0] = -38
            self.direction = 'left'

    def shootdt(self, dt, xf, yf):
                self.shooter1dt = self.shooter1dt + dt
                self.shooter2dt = self.shooter2dt + dt
                if self.shooter1dt >= 0.5:
                    self.shooter1dt = 0

                    if self.direction == 'right':
                        bomb = Gasbomb(self.hitbox.x+63, self.hitbox.y+2, self.direction)
                        bomb.thrw(xf, yf)
                        self.gasbombs.append(bomb)

                    if self.direction == 'left':
                        bomb = Gasbomb(self.hitbox.x-16, self.hitbox.y+2, self.direction)
                        bomb.thrw(xf, yf)
                        self.gasbombs.append(bomb)

                if self.shooter2dt >= 1:
                    self.shooter2dt = 0.5
                    if self.direction == 'right':
                        bomb = Gasbomb(self.hitbox.x+34, self.hitbox.y+6, self.direction)
                        bomb.thrw(xf, yf)
                        self.gasbombs.append(bomb)

                    if self.direction == 'left':
                        bomb = Gasbomb(self.hitbox.x+63, self.hitbox.y+6, self.direction)
                        bomb.thrw(xf, yf)
                        self.gasbombs.append(bomb)

    def update_img_pos(self):
        if self.direction == 'right':
            self.img_pos[0] = self.hitbox.bottomleft[0]-12
            self.hitbox.midbottom = (round(self.pos[0]),round(self.pos[1]))

        if self.direction == 'left':
            self.img_pos[0] = self.hitbox.bottomleft[0]-20
            self.hitbox.midbottom = (round(self.pos[0]),round(self.pos[1]))

    def update_sprites(self):
        if self.direction == 'right':
            self.img = self.Sprites["moving_right"]

        if self.direction == 'left':
            self.img = self.Sprites["moving_left"]

    def drawenemy(self, screen):
        if self.state == 'moving':
            screen.blit(self.img, (self.img_pos[0], self.img_pos[1]))
    
    def update_truck(self, dt, screen, xf, yf):
        self.mvnt(dt)
        self.shootdt(dt, xf, yf)
        self.update_img_pos()
        self.update_sprites()

        for gasbomb in self.gasbombs:
            gasbomb.update_gasbomb(dt)
            gasbomb.drawgasbomb(screen)