import pygame
from ent import Ent
from enemy import Enemy

class Panda(Ent):
    def __init__(self, x, y, bamboo, orientation, speed, is_attacking):
        super().__init__(x, y, bamboo, orientation, speed)
        self.is_attacking = False
        self.speed = 8
        self.sprites = {
            "idle_left": pygame.image.load("PandaPOO/Assets/Panda/panda_idle_left.png"),
            "idle_right": pygame.image.load("PandaPOO/Assets/Panda/panda_idle_right.png"),
            "up_left": pygame.image.load("PandaPOO/Assets/Panda/panda_up_left.png"),
            "up_right": pygame.image.load("PandaPOO/Assets/Panda/panda_up_right.png"),
            "down_left": pygame.image.load("PandaPOO/Assets/Panda/panda_down_left.png"),
            "down_right": pygame.image.load("PandaPOO/Assets/Panda/panda_down_right.png")
        }                           
        
    def move_left(self, bamboo, orientation):
        if self.orientation == 0 and self.bamboo != 1:
            self.orientation = 1 
            self.bamboo -= 1 
        elif self.orientation == 1:
            self.orientation = 0

    def move_right(self, bamboo, orientation):
        if self.orientation == 1 and self.bamboo != 3:
            self.orientation = 0 
            self.bamboo += 1 
        elif self.orientation == 0:
            self.orientation = 1
            
    def move_up(self, y, speed):
        if self.y > 2:
            super().move_up(y, speed)

    def move_down(self, y, speed):    
        if self.y < 752:
            super().move_down(y, speed)

    def update_coor(self, x, bamboo, orientation):
        super().update_coor(x, bamboo, orientation)

    def attack(self, y, speed, is_attacking):
        self.is_attacking = True
        self.speed = 15
        if self.y < 748:
            super().move_down(y, speed)
                              