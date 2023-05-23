import pygame
import random
from master import Master
from ent import Ent
from panda import Panda
from enemy import Enemy

#Inicialización del programa

pygame.init() #Funciones del motor de juegos
pygame.mixer.init() #Sonidos

#Customización de la ventana

screen = pygame.display.set_mode((470, 840)) #Resolucion
pygame.display.set_caption("Panda") #Nombre
icon = pygame.image.load("PandaPOO/Assets/Uses/panda.png") #Imagen del icono
pygame.display.set_icon(icon) #Icono

#Customizacion de elementos dentro de la ventana

background_image = pygame.image.load("PandaPOO/Assets/Uses/background.png") #Imagen de fondo

#Elementos no jugables

bamboo_move_sound = pygame.mixer.Sound("PandaPOO/Assets/Sounds/bamboo_hit.wav") #Sonido de movimiento horizontal
time_font = pygame.font.SysFont("DroidSans", 26) #Fuente del texto de tiempo


#Iniciacion del bucle del juego

running = True

#Declaración de clases y sus atributos dentro del juego

master = Master(0, 0)
panda = Panda(x=0, y=350, bamboo=2, orientation=0, speed=0, is_attacking=False)
enemy = Enemy(x=0, y=0, bamboo=0, orientation=0, speed=4)

#Variables con multiples usos

panda_movement_delay = 10 #Retraso del movimiento horizontal del panda
key_frame_counter = 0  #Contador de fotogramas desde la última tecla horizontal presionada
key_pressed = False #¿Hay alguna tecla siendo presionada?
panda_up = False #¿Esta el panda llendo hacia arriba?
panda_down = False #¿Esta llendo hacia abajo?

#Array vacío para almacenar enemigos
enemies = []

#Bucle del juego

while running == True:
    
    #Configuración de la función de cerrar la ventana, si esto no se agrega, no se puede cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #Eventos de teclas presionadas
        
        #Teclas horizontales
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                key_pressed = True
                
        #Teclas verticales
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                panda_up = False
            elif event.key == pygame.K_DOWN:
                panda_down = False        
        
        
    #Control de acciones de teclas presionadas
    
    keys = pygame.key.get_pressed()
    
    #Se llaman las funciones de la clase correspondiente (panda) cuando se quiere realizar un movimiento
    
    
    #Control del movimiento vertical del panda

    #Arriba
    if keys[pygame.K_UP]:
        panda.move_up(panda.y, panda.speed) #Se llama el metodo de movimiento del panda
        panda_up = True #Se actualiza el estado de movimiento vertical
        
    #Abajo
    if keys[pygame.K_DOWN]: #Todo lo mismo que antes pero hacia abajo
        panda.move_down(panda.y, panda.speed)
        panda_down = True

    #Control del movimiento horizontal del panda
    
    #Izquierda
                                                                  #Solo se puede mover cuando: 
    if key_pressed and key_frame_counter >= panda_movement_delay: #1. El contador de fotogramas alcanza el retraso de movimiento,
        if keys[pygame.K_LEFT] and not panda_up and not panda_down: #2. El panda NO se esta moviendo verticalmente
            
            if not (panda.bamboo == 1 and panda.orientation == 0): #Control del sonido, si el panda no se mueve en realidad, no suena nada
                bamboo_move_sound.play()
            panda.move_left(panda.bamboo, panda.orientation)

        #Derecha
        
        elif keys[pygame.K_RIGHT] and not panda_up and not panda_down: #Todo lo mismo que antes pero hacia la derecha
            if not (panda.bamboo == 3 and panda.orientation == 1):
                bamboo_move_sound.play()
            panda.move_right(panda.bamboo, panda.orientation)
        
        #Luego de terminar de presionar una tecla, reinicia las variables de control
        key_frame_counter = 0  
        key_pressed = False  
        
        
    #Contador
    
    master.time_passed = pygame.time.get_ticks() / 1000 #Extrae la variable de tiempo de las clase Master y la transforma a segundos
    time_text = time_font.render("Tiempo: %d" % master.time_passed, True, (13, 40, 0)) #Texto que se va a dibujar para el contador
    
    
    #Función que actualiza el sistema de coordenadas de las "entities" llamando sus metodos
    
    panda.update_coor(panda.x, panda.bamboo, panda.orientation)
    enemy.update_coor(enemy.x, enemy.bamboo, enemy.orientation) 
        
    #Control de sprites del panda según la posición horizontal y movimiento vertical    
    
    if panda_up == False and panda_down == False:
        if panda.orientation == 0:
            sprite = panda.sprites["idle_left"]
        elif panda.orientation == 1:
            sprite = panda.sprites["idle_right"]
    elif panda_up == True:
        if panda.orientation == 0:
            sprite = panda.sprites["up_left"]
        elif panda.orientation == 1:
            sprite = panda.sprites["up_right"]
    elif panda_down == True:
        if panda.orientation == 0:
            sprite = panda.sprites["down_left"]
        elif panda.orientation == 1:
            sprite = panda.sprites["down_right"]
            
    #Despues de todo, incrementa el contador de fotogramas en 1
    key_frame_counter += 1
        
    #Calcula el tamaño rectangular que debe ocupar el panda
    panda.rect = sprite.get_rect()
    panda.rect.x = panda.x
    panda.rect.y = panda.y
    
    #Calcula el tamaño rectangular que deben ocupar los enemigos
    enemy.rect = sprite.get_rect()
    enemy.rect.x = enemy.x
    enemy.rect.y = enemy.y
            
    #Dibujar los elementos en pantalla, primero el fondo para que los demás elementos aparezcan por encima de este
    screen.blit(background_image, (0, 0))  
    
    #Luego el texto
    screen.blit(time_text, (5, 10)) 
    
    #Por ultimo, el panda y los enemigos
    screen.blit(sprite, (panda.x, panda.y)) 
    
                
    #Actualizar la información visual en pantalla para que se dibuje en el monitor
    pygame.display.flip()
    
    #Este ciclo se repite 60 veces cada segundo