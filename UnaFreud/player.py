# se importa la libreria sobre la cual correrá el programa
import pygame
from physics import Physics
from levels import Objects
from bottles import Bottles
from scores import scores
pygame.init()
physics = Physics()
object = Objects()

#Clase que definirá al jugador y sus mecanicas
class Player:
    def __init__(self):
        #Velocidad del jugador
        self.v = [0, 0]

        #Defino los atributos del jugador
        self.pos = [50, 140]
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.health = 100
        self.alive = True
        self.inatack = False
        self.inmortal = False
        self.inmortaldt = 0
        self.shooterdt = 0

        #Sizes para la hitbox segun el estado del jugador
        self.stationary_size = (6, 30)
        self.sprinting_size = (12, 20)
        self.crouched_size = (8, 8)
        self.bottles = []
        self.v0x = 0
        self.v0y = 0

        #Hitbox 
        self.hitbox = pygame.Rect(46, 124, 6, 30)
        self.hitbox.size = (6, 30)
        self.hitbox.midbottom = self.pos

        self.can_thrw = True

        #Variable  para determinar la orientacion en la que ve el jugador
        self.direction = 'right'

        #Variable para determinar la direccion del objeto arrojadizo
        self.direction_thrw = self.direction

        #Variable para identificar el estado del jugador
        self.state = 'stationary'

        #IMAGENES
        self.Sprites = {
            "stationary_right": pygame.image.load("Pygame/UnaFreud/Assets/Player/Stationary_Right.png").convert_alpha(),

            "stationary_left": pygame.image.load("Pygame/UnaFreud/Assets/Player/Stationary_Left.png").convert_alpha(),

            "crouched_right": pygame.image.load("Pygame/UnaFreud/Assets/Player/Crouched_Right.png").convert_alpha(),

            "crouched_left": pygame.image.load("Pygame/UnaFreud/Assets/Player/Crouched_Left.png").convert_alpha(),

            "sprinting_right": pygame.image.load("Pygame/UnaFreud/Assets/Player/Sprint_1_right.png").convert_alpha(),

            "sprinting_left": pygame.image.load("Pygame/UnaFreud/Assets/Player/Sprint_1_left.png").convert_alpha(),

            "inatack_right": pygame.image.load("Pygame/UnaFreud/Assets/Player/inatack_right.png").convert_alpha(),

            "inatack_left": pygame.image.load("Pygame/UnaFreud/Assets/Player/inatack_left.png").convert_alpha(),
        }  

        #Jugador
        self.img = pygame.image.load("Pygame/UnaFreud/Assets/Player/Stationary_Right.png").convert_alpha();
#============================================================================================================================================================================================================================================
    #MECANICAS

    #Gravedad aplicada
    def grvty(self, dt):
        #Calcula velocidad en y
        self.v[1] = self.v[1]+physics.g*dt
    
    #Movimiento en x,y
    def mvnt(self, dt):
        self.pos[0] = self.pos[0]+self.v[0]*dt
        self.pos[1] = self.pos[1]+self.v[1]*dt

    #Creación del arrojadizo
    def shootdt(self, dt):
        self.shooterdt = self.shooterdt+dt
        if shooterdt >= 0.5:
            shooterdt = 0
            self.can_thrw = True

    def thrw(self):
        bottle = Bottles(self.hitbox.centerx, self.hitbox.centery, self.v0x, self.v0y)
        self.bottles.append(bottle)
    
    #Colisiones
    def collisions(self):
        #Limite izquierdo
        if self.pos[0] < self.hitbox.width/2:
            self.pos[0] = self.hitbox.width/2
            self.hitbox.midbottom = (self.pos[0], self.pos[1])
            self.v[0] = 0

        #Limite derecho
        if self.pos[0] > 304-(self.hitbox.width/2):
            self.pos[0] = (304-self.hitbox.width/2)
            self.v[0] = 0

        #Limite inferior
        if self.pos[1] > object.floor:
            self.v[1] = 0
            self.pos[1] = object.floor

    #Deteccion y asignacion de teclas mantenidas y clicks
    def input(self,keys):
        #Agacharse
        if keys[pygame.K_s]:
            if self.state != 'crouched':
                self.hitbox.size = self.crouched_size
                self.hitbox.midbottom = self.pos
                self.state = 'crouched'
    
        #Trotar hacia la derecha
        if keys[pygame.K_d]:
            self.direction = 'right'
            if self.state != 'crouched':
                self.v[0] = 168
                self.state = 'sprinting'
                self.hitbox.size = self.sprinting_size
                self.hitbox.midbottom = self.pos
            else:
                self.v[0] = 28

        #Trotar hacia la izquierda
        if keys[pygame.K_a]:
            self.direction = 'left'
            
            if self.state != 'crouched':
                self.v[0] = -168
                self.state = 'sprinting'
                self.hitbox.size = self.sprinting_size
                self.hitbox.midbottom = self.pos
            else:
                self.v[0] = -28

        #Correr
        if keys[pygame.K_LSHIFT]:
            #Correr hacia la derecha
            if keys[pygame.K_d]:
                if self.state != 'crouched':
                    self.v[0] = 408
                    self.state = 'sprinting'
                    self.hitbox.size = self.sprinting_size
                    self.hitbox.midbottom = self.pos
                
                else:
                    self.v[0] = 63

            #Correr hacia la izquierda
            if keys[pygame.K_a]:
                if self.state != 'crouched':
                    self.v[0] = -408
                    self.state = 'sprinting'
                    self.hitbox.size = self.sprinting_size
                    self.hitbox.midbottom = self.pos
                else:
                    self.v[0] = -63

    #Deteccion y asignacion de teclas de un pulso
    def KEYDOWN(self, event):
            #Detecto cuando se presiona una tecla
            if event.type == pygame.KEYDOWN:
                #Salto
                if event.key == pygame.K_SPACE:
                    if self.pos[1] == object.floor:
                        self.v[1] = -211

                #Girar a la derecha
                if event.key == pygame.K_d:
                    self.direction = 'right'
                    self.v0x = 200
                    if self.state != 'crouched':
                        self.state = 'sprinting'
                        self.hitbox.size = self.sprinting_size
                        self.hitbox.midbottom = self.pos

                #Girar a la izquierda
                if event.key == pygame.K_a:
                    self.direction = 'left'
                    self.v0x = -200
                    if self.state != 'crouched':
                        self.state = 'sprinting'
                        self.hitbox.size = self.sprinting_size
                        self.hitbox.midbottom = self.pos

                if event.key == pygame.K_w:
                    self.v0y = -220
                
                if event.key == pygame.K_e:
                    self.v0x = 200
                
                if event.key == pygame.K_q:
                    self.v0x = -200
    def MOUSEDOWN(self, event):
        #Deteccion de mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
                self.thrw()

    def KEYUP(self, event):
            #Detecta cuando se deja de presionar una tecla
            if event.type == pygame.KEYUP:
                #Devuelvo el tamaño original del personaje luego de agacharse
                if event.key == pygame.K_s:
                    self.hitbox.size = self.stationary_size
                    self.hitbox.midbottom = self.pos
                    self.state = 'stationary'

                #Devuelvo la velocidad original al personaje
                if event.key == pygame.K_d:
                    self.v[0] = 0
                    if self.state != 'crouched':
                        self.state = 'stationary'
                        self.hitbox.size = self.stationary_size
                        self.hitbox.midbottom = self.pos

                #Devuelvo la velocidad original al personaje
                if event.key == pygame.K_a:
                    self.v[0] = 0                   
                    if self.state != 'crouched':
                        self.state = 'stationary'
                        self.hitbox.size = self.stationary_size
                        self.hitbox.midbottom = self.pos

                if event.key == pygame.K_w:
                    self.v0y = 0
    
    def damage(self, amount):
        if not self.inmortal:
            self.inmortal = True
            self.inmortaldt = 0
            self.health = self.health-amount
            scores.score = scores.score - 1000
            
        if self.health <= 0:
            self.alive = False
            return self.alive
        
    #Actualizo la imagen del jugador en base a su estado
    def update_sprites(self):
        #Si esta parado
        if self.state == 'stationary':
            if self.direction == 'right':
                self.img = self.Sprites["stationary_right"]
            elif self.direction == 'left':
                self.img = self.Sprites["stationary_left"]

        if self.inatack == True:

            if self.state == 'stationary':

                if self.direction == 'right':
                    self.img = self.Sprites["stationary_right"]
                elif self.direction == 'left':
                    self.img = self.Sprites["stationary_left"]

        #si esta sprintando
        if self.state == 'sprinting':
            if self.direction == 'right':
                self.img = self.Sprites["sprinting_right"]
            elif self.direction == 'left':
                self.img = self.Sprites["sprinting_left"]

        #Si esta siendo herido
        if self.inatack == True:
            if self.direction == 'right':
                self.img = self.Sprites["inatack_right"]
            elif self.direction == 'left':
                self.img = self.Sprites["inatack_left"]
                
        #Si esta agachado
        if self.state == 'crouched':
            if self.direction == 'right':
                self.img = self.Sprites["crouched_right"]
            elif self.direction == 'left':
                self.img = self.Sprites["crouched_left"]

    #Dibujo al jugador
    def drawplayer(self, screen):
        if self.state == 'stationary':
            screen.blit(self.img, (self.hitbox.x-5, self.hitbox.y-9))

        elif self.state == 'sprinting':
            screen.blit(self.img, (self.hitbox.x-12, self.hitbox.y-5))
        
        elif self.state == 'crouched':
            screen.blit(self.img, (self.hitbox.x-4, self.hitbox.y-8))

        elif self.inatack == True:
            screen.blit(self.img, (self.hitbox.x-5, self.hitbox.y-9))

        for bottle in self.bottles:
            bottle.drawbottle(screen)

    #Funcion que recopila todas las funciones/mecanicas del jugador para un manejo mas limpio en main.py
    def update_player(self,dt):
        
        #Actualizo las posiciones actuales
        self.hitbox.midbottom = round(self.pos[0]), round(self.pos[1])

        if self.inmortal:
            self.inmortaldt = self.inmortaldt+dt

            if self.inmortaldt >= 0.5:
                self.inmortal = False
                self.inmortaldt = 0

        self.grvty(dt)
        self.mvnt(dt)
        self.collisions()
        self.update_sprites()
        self.inatack = False

        if self.can_thrw == False:
            self.shootdt(dt)

        for bottle in self.bottles:
            bottle.update_bottles(dt)
