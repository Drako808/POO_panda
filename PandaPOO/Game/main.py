import pygame
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

panda.rect = panda.sprites["idle_left"].get_rect()

movement_delay = 10  
frame_counter = 0  
key_pressed = False
up = False
down = False

while running == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                key_pressed = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            elif event.key == pygame.K_DOWN:
                down = False        
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        panda.move_up(panda.y, panda.speed)
        up = True

    if keys[pygame.K_DOWN]:
        panda.move_down(panda.y, panda.speed)
        down = True

    
    if key_pressed and frame_counter >= movement_delay:
        if keys[pygame.K_LEFT] and not up and not down:
            panda.move_left(panda.bamboo, panda.orientation)
        elif keys[pygame.K_RIGHT] and not up and not down:
            panda.move_right(panda.bamboo, panda.orientation)


            
        frame_counter = 0  
        key_pressed = False  
        
    frame_counter += 1
            
    if panda.bamboo == 1 and panda.orientation == 0:
        panda.x = 42
        
    elif panda.bamboo == 2 and panda.orientation == 0:
        panda.x = 185
        
    elif panda.bamboo == 3 and panda.orientation == 0:
        panda.x = 329

    elif panda.bamboo == 1 and panda.orientation == 1:
        panda.x = 77

    elif panda.bamboo == 2 and panda.orientation == 1:
        panda.x = 220

    elif panda.bamboo == 3 and panda.orientation == 1:
        panda.x = 364
        
    if up == False and down == False:
        if panda.orientation == 0:
            sprite = panda.sprites["idle_left"]
        elif panda.orientation == 1:
            sprite = panda.sprites["idle_right"]
    elif up == True:
        if panda.orientation == 0:
            sprite = panda.sprites["up_left"]
        elif panda.orientation == 1:
            sprite = panda.sprites["up_right"]
    elif down == True:
        if panda.orientation == 0:
            sprite = panda.sprites["down_left"]
        elif panda.orientation == 1:
            sprite = panda.sprites["down_right"]
            

        
    panda.rect = sprite.get_rect()
    panda.rect.x = panda.x
    panda.rect.y = panda.y
            
    screen.blit(background_image, (0, 0))  
    screen.blit(sprite, (panda.x, panda.y))
    pygame.display.flip()