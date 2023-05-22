import pygame
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
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(background_image, (0, 0))  
    pygame.display.flip()