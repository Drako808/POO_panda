#Importar los modulos basicos de python.

import os #Modulo de sistema operativo para manejar la ubicacion del icono del juego.
import pygame #Modulo para controlar funciones graficas, de ventanas y de teclas. Diseñado para hacer juegos.
import random #Modulo de funciones aleatorias.
from tkinter import messagebox #Modulo de funciones de visualizacion de elementos. En este caso se importa una caja de texto.

#Importar los modulos de las clases del juego.

from master import Master #Control de las funciones basicas del juego que no afectan directamente la jugabilidad (revisar master.py).
from ent import Ent #Del ingles Entity (Entidad). Se refiere a los objetos "vivos" del juego (revisar ent.py).
from panda import Panda #Jugador (revisar panda.py)
from enemy import Enemy #Enemigo (revisar enemy.py)

#Inicializacion de pygame y su modulo de sonido.

pygame.init()
pygame.mixer.init()


#Configuracion de la ventana de juego.

screen = pygame.display.set_mode((470, 840)) #Tamaño de la ventana.
pygame.display.set_caption("Panda") #Nombre de la ventana
icon_path = os.path.abspath("PandaPOO/Assets/Uses/panda.png") #Señalar en que directorio se encuentra el icono por medio de un path absoluto.
icon = pygame.image.load(icon_path) #Cargar el icono a una variable.
pygame.display.set_icon(icon) #Poner la variable como icono en la ventana.

#Configuracion basica del juego.

background_image = pygame.image.load("PandaPOO/Assets/Uses/background.png") #Imagen de fondo.

#Sonidos y fuente del texto.
bamboo_move_sound = pygame.mixer.Sound("PandaPOO/Assets/Sounds/bamboo_hit.wav")
splat_sound = pygame.mixer.Sound("PandaPOO/Assets/Sounds/splat.wav")
font = pygame.font.SysFont("DroidSans", 26)

#Variables del juego.

enemies = [] #Lista vacia para almacenar enemigos.

#Sacar a las clases de sus modulos respectivos y otorgarles variables iniciales. No es necesario con la clase Enemy, ya que sus variables son determinadas aleatoriamente.
master = Master(0, 0)
panda = Panda(x=0, y=350, bamboo=2, orientation=0, speed=0, is_attacking=False)

#Variables con multiples usos para mejorar la jugabilidad.

panda_movement_delay = 10
key_frame_counter = 0
spawn_timer = int
key_pressed = False
panda_up = False
panda_down = False
panda_attack = False


#Bucle principal del juego (siempre inicia de la misma manera). 

running = True #Se inicia con la variable "corriendo" a True.
while running: #Todo dentro de este bucle se repite cada fotograma hasta que se cierra el juego (cuando "corriendo" deja de ser True)
    
    for event in pygame.event.get(): #Establecer que pygame reconozca los inputs del jugador.
        
        if event.type == pygame.QUIT: #Configuracion para poder cerrar la ventana del juego como cualquier otra ventana.
            running = False
            
        #Configuracion de los eventos de las teclas de juego    
                
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                key_pressed = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                panda_up = False
            elif event.key == pygame.K_DOWN:
                panda_down = False        
            elif event.key == pygame.K_x:
                panda.speed = 8
                panda_down = False
                panda.is_attacking = False
        
    #Configuracion de las funciones dentro del juego que ocurren con los eventos de las teclas.    
        
    keys = pygame.key.get_pressed() #Cargar los eventos de teclas a una variable.
    
    if keys[pygame.K_UP]:
        panda.move_up(panda.y, panda.speed)
        panda_up = True
    
    if keys[pygame.K_DOWN]:
        panda.move_down(panda.y, panda.speed)
        panda_down = True        
    
    if keys[pygame.K_x]:
        panda.attack(panda.speed, panda.y, panda.is_attacking)
        panda_down = True 
    
    if key_pressed and key_frame_counter >= panda_movement_delay:
        if keys[pygame.K_LEFT] and not panda_up and not panda_down:
            if not (panda.bamboo == 1 and panda.orientation == 0):
                bamboo_move_sound.play()
            panda.move_left(panda.bamboo, panda.orientation)
        elif keys[pygame.K_RIGHT] and not panda_up and not panda_down:
            if not (panda.bamboo == 3 and panda.orientation == 1):
                bamboo_move_sound.play()
            panda.move_right(panda.bamboo, panda.orientation)
            
        key_frame_counter = 0
        key_pressed = False
    
    
    #Poner las variables de tiempo y puntaje de la clase Master como texto en pantalla.
    
    master.time_passed = pygame.time.get_ticks() / 1000
    time_text = font.render("Tiempo: %d" % master.time_passed, True, (13, 40, 0))
    score_text = font.render("Puntaje: %d" % master.score, True, (13, 40, 0))
    
    
    #Sacar un enemigo de la clase Master con un intervalo aleatorio de tiempo.
    
    if spawn_timer == 0:
        enemy = master.spawn_enemy(Enemy)  
        enemies.append(enemy) 
        spawn_timer = 1
    else:
        spawn_timer = random.randint(0, 40)
     
     
    #Dibujar en pantalla el fondo, el texto de tiempo y el texto de puntaje, en ese orden.
    
    screen.blit(background_image, (0, 0))
    screen.blit(time_text, (5, 10))
    screen.blit(score_text, (370, 10))
    
    
    #Sistema para actualizar la posicion en pantalla y el sprite de el panda según su orientacion y estado de moviemiento.
    
    panda.update_coor(panda.x, panda.bamboo, panda.orientation)
    
    if panda_up == False and panda_down == False:
        if panda.orientation == 0:
            panda_sprite = panda.sprites["idle_left"]
        elif panda.orientation == 1:
            panda_sprite = panda.sprites["idle_right"]
    elif panda_up == True:
        if panda.orientation == 0:
            panda_sprite = panda.sprites["up_left"]
        elif panda.orientation == 1:
            panda_sprite = panda.sprites["up_right"]
    elif panda_down == True or panda.is_attacking == True:
        if panda.orientation == 0:
            panda_sprite = panda.sprites["down_left"]
        elif panda.orientation == 1:
            panda_sprite = panda.sprites["down_right"]
    
    #Calculo del espacio rectangular que ocupa el panda segun sus coordenadas.
    panda.rect = panda_sprite.get_rect()
    panda.rect.x = panda.x
    panda.rect.y = panda.y
    
    #Dibujar al panda.
    screen.blit(panda_sprite, (panda.x, panda.y))
    
    
    #Lo mismo que el sistema de el panda, pero se repite para cada enemigo en la lista de enemigos.
    
    for enemy in enemies:
        
        if enemy.orientation == 0:
            enemy_sprite = enemy.sprites["left"]
        else:
            enemy_sprite = enemy.sprites["right"]
        
        enemy.rect = enemy_sprite.get_rect()
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.y      

        #A diferencia de el panda, primero se dibuja el enemigo en pantalla, y luego se actualiza su posicion.
        #Es probable que esta inconsistencia sea lo que causa que los enemigos en pantalla parpadeen pero el panda no.
        screen.blit(enemy_sprite, (enemy.x + 28, enemy.y)) 
        enemy.update_coor(enemy.x, enemy.bamboo, enemy.orientation)
        enemy.move_up(enemy.y, enemy.speed)     
        
        
        #Comprobar las colisiones del panda y los enemigos, si el panda está atacando, el enemigo muere y se obtiene un punto,
        #de lo contrario, ocurre un game over.
        
        if enemy.bamboo == panda.bamboo and enemy.orientation == panda.orientation:
            if panda.rect.colliderect(enemy.rect):
                if panda.is_attacking and enemy in enemies:
                    splat_sound.play()
                    enemies.remove(enemy)
                    master.score += 1
                else:
                    running = False
                    messagebox.showinfo("Game Over", f"Puntaje: {master.score}\n" f"Tiempo: {int(master.time_passed)}")
                    
                    
                    
    key_frame_counter += 1
        
    #Poner los objetos dibujados en el monitor.
    pygame.display.flip()