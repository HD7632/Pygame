import pygame
from levels import Objects
from physics import Physics
pygame.init()
physics = Physics()
object = Objects()

class Gasbombs:
    def __init__(self, x, y, shoot_direction):
        self.pos = [x, y]
        self.vx = 1
        self.vy = 0
        self.direction = shoot_direction
        self.hitbox = pygame.Rect(x, y, 3, 3)

    #Gravedad aplicada
    def grvty(self, dt):
        
        #Calcula velocidad en y
        self.vy = self.vy+physics.g*dt

    def thrw(self, xf, yf):
        
        if self.direction == 'right':
            self.vx = -120

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
        
        self.hitbox.x = self.hitbox.x+self.vx*dt
        
        self.hitbox.y = self.hitbox.y+self.vy*dt
