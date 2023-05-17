import pygame

pygame.init()

screen = pygame.display.set_mode((470, 840))

pygame.display.set_caption("Panda")
icon = pygame.image.load("PandaPOO/Assets/panda.png")
pygame.display.set_icon(icon)
background_image = pygame.image.load("PandaPOO/Assets/fondo.png")

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(background_image, (0, 0))  
    pygame.display.flip()