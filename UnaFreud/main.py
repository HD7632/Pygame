# se importa la libreria sobre la cual correrá el programa
import pygame
from player import Player
from levels import Objects
from menus import Pmenu
from menus import Psmenu
from menus import Dftmenu
from menus import Wnmenu
from enemy import Truck
from physics import Physics
from scores import scores
pygame.init()

#le pongo nombre a la ventana del programa
pygame.display.set_caption("UnaFreud")

#Booleano que define si se esta jugando o no
runningcode = True 

#Estados del programa
state = 'pmenu'

#Defino los nombres de los objetos de diversas clases
object = Objects()
player = Player()
pmenu = Pmenu()
psmenu = Psmenu()
dftmenu = Dftmenu()
wnmenu = Wnmenu()
truck = Truck()
physics = Physics()

remove = False
fuente = pygame.font.SysFont("Agency FB", 15)
superficie_texto1 = fuente.render("¡Perdiste!", True, (255, 0, 0))
superficie_texto2 = fuente.render("Reprobaste Paro En Varias Variables", True, (255, 0, 0))
superficie_texto3 = fuente.render("Pasaste!!!, sigue EnTroplia", True, (0, 255, 0))
shoot_direction = ''

while runningcode:
    #Defino el delta de tiempo y cuantos ticks por segundo
    dt = object.clock.tick(60)/1000
    
    #Inicializacion de partida
    if state == 'play':
        #Limpio imagen
        object.screen.blit(object.bkgr_1, (0,0))

        #Defino la deteccion y funcionamiento cuando una tecla se mantiene oprimida
        keys = pygame.key.get_pressed()
        player.input(keys)

        #Deteccion de teclas y de mouse
        for event in pygame.event.get():
            #Programo que el juego se cierre cuando el usuario haga clic en la x de la ventana
            if event.type == pygame.QUIT:
                runningcode = False
            
            #Detecto cuando se presiona una tecla
            if event.type == pygame.KEYDOWN:
                #Abir menu de pausa
                if event.key == pygame.K_ESCAPE:
                    state = 'pause'
                #Defino la deteccion y funcionamiento cuando una tecla se oprime
                player.KEYDOWN(event)

            #Detecta cuando se deja de presionar una tecla
            if event.type == pygame.KEYUP:
                player.KEYUP(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                player.MOUSEDOWN(event)

        #Actualizo al jugador
        player.update_player(dt)

        xf = player.hitbox.midbottom[0]
        yf = player.hitbox.midbottom[1]

        #Actualizo al camion
        truck.update_truck(dt, object.screen, xf, yf, shoot_direction)

        #llamo a la funcion para actualizar los datos del puntaje
        scores.update_score(dt)
        scores.drawscore(object.screen)

        for gasbomb in truck.gasbombs[:]:
        
            if player.hitbox.colliderect(gasbomb.hitbox):
                player.damage(10)
                player.inatack = True
                player.state = 'stationary'
                player.hitbox.size = player.stationary_size
                player.hitbox.midbottom = player.pos
                remove = True

            if gasbomb.hitbox.x <= 0:
                remove = True

            if gasbomb.hitbox.x >= object.width:
                remove = True

            if gasbomb.hitbox.y >= object.floor:
                remove = True

            if remove == True:
                truck.gasbombs.remove(gasbomb)
                remove = False

        if player.hitbox.colliderect(truck.hitbox):
            player.damage(5)
            player.inatack = True
            player.state = 'stationary'
            player.hitbox.size = player.stationary_size
            player.hitbox.midbottom = player.pos

        for bottle in player.bottles:
            if truck.hitbox.colliderect(bottle.hitbox):
                truck.damage(10)

        if truck.alive == False:
            state = 'won'

        if player.alive == False:
            state = 'defeat'

        #Llamo a la funcion para dibujar el juego
        truck.drawenemy(object.screen)
        player.drawplayer(object.screen)

        #Muestro lo dibujado
        pygame.display.flip()

    if state == 'defeat':
        object.screen.fill((0,0,0))
        object.screen.blit(superficie_texto1, (130, 56))
        object.screen.blit(superficie_texto2, (80, 112))
        #Deteccion de teclas y de mouse
        for event in pygame.event.get():
            #Programo que el juego se cierre cuando el usuario haga clic en la x de la ventana
            if event.type == pygame.QUIT:
                runningcode = False

            #Deteccion de mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Configuracion del boton "exit"
                if pmenu.xtbt.collidepoint(event.pos):
                    runningcode = False
        
        #Llamo a la funcion para dibujar el menu principal
        dftmenu.drawdefeat(object.screen)
        pygame.display.flip()

    if state == 'won':
        #Limpio imagen
        object.screen.fill((30, 30, 30))
        object.screen.blit(superficie_texto3, (76, 56))

        #Deteccion de teclas y de mouse
        for event in pygame.event.get():
            #Programo que el juego se cierre cuando el usuario haga clic en la x de la ventana
            if event.type == pygame.QUIT:
                runningcode = False
        
            #Deteccion de mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Configuracion del boton "play"
                if pmenu.stbt.collidepoint(event.pos):
                    state = 'play'
        
                #Configuracion del boton "exit"
                if pmenu.xtbt.collidepoint(event.pos):
                    runningcode = False
                
        #Llamo a la funcion para dibujar el menu principal
        wnmenu.drawwon(object.screen)
        
        #Muestro lo dibujado
        pygame.display.flip()
    #Inicializacion del menu principal
    if state == 'pmenu':

        #Limpio imagen
        object.screen.fill((30, 30, 30))

        #Deteccion de teclas y de mouse
        for event in pygame.event.get():
            #Programo que el juego se cierre cuando el usuario haga clic en la x de la ventana
            if event.type == pygame.QUIT:
                runningcode = False

            #Deteccion de mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Configuracion del boton "play"
                if pmenu.stbt.collidepoint(event.pos):
                    state = 'play'

                #Configuracion del boton "exit"
                if pmenu.xtbt.collidepoint(event.pos):
                    runningcode = False
        
        #Llamo a la funcion para dibujar el menu principal
        pmenu.drawmenu(object.screen)

        #Muestro lo dibujado
        pygame.display.flip()

    if state == 'pause':
        #Deteccion de teclas y de mouse
        for event in pygame.event.get():
            #Programo que el juego se cierre cuando el usuario haga clic en la x de la ventana
            if event.type == pygame.QUIT:
                runningcode = False

            #Cerrar menu de pausa
            if event.type == pygame.K_ESCAPE:
                    state = 'play'

            #Deteccion de mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Configuracion del boton "continue"
                if psmenu.stbt.collidepoint(event.pos):
                    state = 'play'

                #Configuracion del boton "exit"
                if psmenu.xtbt.collidepoint(event.pos):
                    state = 'pmenu'

        #Llamo a la funcion para dibujar el menu
        psmenu.drawpause(object.screen)

        #Muestro lo dibujado
        pygame.display.flip()
#Termino el programa
pygame.quit()
