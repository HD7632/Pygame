import pygame
from physics import Physics

physics = Physics()
class Bottles:
    def __init__(self, x, y, v0x, x0y):
        self.pos = [x, y]
        self.vx = 1
        self.vy = 0
        self.hitbox = pygame.Rect(x, y, 5, 5)

    def grvty(self, dt):
        self.vy = self.vy+physics.g*dt

    def drawbottle(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.hitbox)

    def update_bottles(self, dt):
        self.grvty(dt)
        self.pos[0] = self.pos[0]+self.vx*dt
        self.pos[1] = self.pos[1]+self.vy*dt
        self.drawbottle
