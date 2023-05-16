import pygame

pygame.init()

screen = pygame.display.set_mode((470, 840))

pygame.display.set_caption("Panda")
icon = pygame.image.load("panda.png")
pygame.display.set_icon(icon)

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 200, 0))
    pygame.display.update()