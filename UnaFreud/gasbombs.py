import pygame
import math
from levels import Objects
from physics import Physics
physics = Physics()
object = Objects()

class Gasbomb:
    def __init__(self, x, y, direction):
        self.pos = [x, y]
        self.vx = 0
        self.vy = 0
        self.direction = direction
        self.hitbox = pygame.Rect(x, y, 5, 5)

    #Gravedad aplicada
    def grvty(self, dt):
        #Calcula velocidad en y
        self.vy = self.vy+physics.g*dt

    def thrw(self, xf, yf):
        if self.direction == 'right':
            self.vx = 120

        elif self.direction == 'left':
            self.vx = -120

        t = (xf-self.hitbox.x)/self.vx
            
        if t <= 0:
            return
        
        if t > 0:
            v0y = ((yf-self.hitbox.y)-((1/2)*physics.g*(t**2)))/t
            self.vy = v0y
        
    def drawgasbomb(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.hitbox)

    def update_gasbomb(self, dt):
        self.grvty(dt)
        print("antes:", self.hitbox.x, self.vx)
        self.hitbox.x = self.hitbox.x+self.vx*dt
        print("después:", self.hitbox.x)
        self.hitbox.y = self.hitbox.y+self.vy*dt
        print(self.direction, self.vx, self.hitbox.x)