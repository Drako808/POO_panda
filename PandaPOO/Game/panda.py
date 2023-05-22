import pygame
from ent import Ent
from enemy import Enemy

class Panda(Ent):
    def __init__(self, y, bamboo, orientation, speed, is_attacking):
        super().__init__(y, bamboo, orientation, speed)
        self.is_attacking = False
        self.speed = 40
        self.sprites = {
            "idle_left": pygame.image.load("PandaPOO/Assets/Panda/panda_idle_left.png"),
            "idle_right": pygame.image.load("PandaPOO/Assets/Panda/panda_idle_right.png"),
            "up_left": pygame.image.load("PandaPOO/Assets/Panda/panda_up_left.png"),
            "up_right": pygame.image.load("PandaPOO/Assets/Panda/panda_up_right.png"),
            "down_left": pygame.image.load("PandaPOO/Assets/Panda/panda_down_left.png"),
            "down_right": pygame.image.load("PandaPOO/Assets/Panda/panda_down_right.png")
        }                               
        
    def move_left(self, bamboo, orientation):
        if bamboo != 1 and bamboo == 0:       
            bamboo -= 1
            
        if orientation == 1:
            orientation = 0
    
    def move_right(self, bamboo, orientation):     
        if bamboo != 3 and orientation == 1:       
            bamboo += 1
            
        if orientation == 0:
            orientation = 1
                        
    def attack(self, y, velocidad):
        atacando = True
        velocidad = 60
        move_down()
        if y == y.enemy + 0.9:
            enemy.recibir_dano()        
            
            
    def die(self):  
        master.game_over()     