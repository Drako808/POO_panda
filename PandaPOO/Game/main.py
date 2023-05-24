#Inicialización del código

import os
import pygame
import random
from tkinter import messagebox
from master import Master
from ent import Ent
from panda import Panda
from enemy import Enemy

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((470, 840))
pygame.display.set_caption("Panda")
icon_path = os.path.abspath("PandaPOO/Assets/Uses/panda.png")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)

background_image = pygame.image.load("PandaPOO/Assets/Uses/background.png")

bamboo_move_sound = pygame.mixer.Sound("PandaPOO/Assets/Sounds/bamboo_hit.wav")
splat_sound = pygame.mixer.Sound("PandaPOO/Assets/Sounds/splat.wav")
font = pygame.font.SysFont("DroidSans", 26)

enemies = []

master = Master(0, 0)
panda = Panda(x=0, y=350, bamboo=2, orientation=0, speed=0, is_attacking=False)

panda_movement_delay = 10
key_frame_counter = 0

spawn_timer = int

key_pressed = False
panda_up = False
panda_down = False
panda_attack = False


#Bucle principal del juego

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
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
        
    keys = pygame.key.get_pressed()
    
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
        
    master.time_passed = pygame.time.get_ticks() / 1000
    time_text = font.render("Tiempo: %d" % master.time_passed, True, (13, 40, 0))
    score_text = font.render("Puntaje: %d" % master.score, True, (13, 40, 0))
    
    if spawn_timer == 0:
        enemy = master.spawn_enemy(Enemy)  
        enemies.append(enemy) 
        spawn_timer = 1
    else:
        spawn_timer = random.randint(0, 40)
     
    screen.blit(background_image, (0, 0))
    screen.blit(time_text, (5, 10))
    screen.blit(score_text, (370, 10))
    
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
    
    panda.rect = panda_sprite.get_rect()
    panda.rect.x = panda.x
    panda.rect.y = panda.y
    
    screen.blit(panda_sprite, (panda.x, panda.y))
    
    for enemy in enemies:
        
        if enemy.orientation == 0:
            enemy_sprite = enemy.sprites["left"]
        else:
            enemy_sprite = enemy.sprites["right"]
        
        enemy.rect = enemy_sprite.get_rect()
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.y      

        screen.blit(enemy_sprite, (enemy.x + 28, enemy.y)) 
        enemy.update_coor(enemy.x, enemy.bamboo, enemy.orientation)
        enemy.move_up(enemy.y, enemy.speed)     
        
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
        
    
    pygame.display.flip()