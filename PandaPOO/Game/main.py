import pygame
import random
from master import Master
from ent import Ent
from panda import Panda
from enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((470, 840))

pygame.display.set_caption("Panda")
icon = pygame.image.load("PandaPOO/Assets/Uses/panda.png")
pygame.display.set_icon(icon)
background_image = pygame.image.load("PandaPOO/Assets/Uses/background.png")

running = True

master = Master(0, 0)
panda = Panda(x=0, y=350, bamboo=2, orientation=0, speed=0, is_attacking=False)
enemy = Enemy(x=0, y=0, bamboo=0, orientation=0, speed=4)

panda.rect = panda.sprites["idle_left"].get_rect()

panda_movement_delay = 10  
frame_counter = 0  
key_pressed = False
panda_up = False
panda_down = False

enemies = []

while running == True:
    
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
    
    panda.update_coor(panda.x, panda.bamboo, panda.orientation)
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        panda.move_up(panda.y, panda.speed)
        panda_up = True

    if keys[pygame.K_DOWN]:
        panda.move_down(panda.y, panda.speed)
        panda_down = True

    
    if key_pressed and frame_counter >= panda_movement_delay:
        if keys[pygame.K_LEFT] and not panda_up and not panda_down:
            panda.move_left(panda.bamboo, panda.orientation)
        elif keys[pygame.K_RIGHT] and not panda_up and not panda_down:
            panda.move_right(panda.bamboo, panda.orientation)

        frame_counter = 0  
        key_pressed = False  
        
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
            
    frame_counter += 1
        
    panda.rect = sprite.get_rect()
    panda.rect.x = panda.x
    panda.rect.y = panda.y
    
    enemy.rect = sprite.get_rect()
    enemy.rect.x = enemy.x
    enemy.rect.y = enemy.y
            
    screen.blit(background_image, (0, 0))  
    
    screen.blit(sprite, (panda.x, panda.y))
                

    pygame.display.flip()