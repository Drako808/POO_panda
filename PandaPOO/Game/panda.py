import pygame
from ent import Ent
from enemy import Enemy

class Panda(Ent):
    def __init__(self, x, y, bamboo, orientation, speed, is_attacking):
        super().__init__(x, y, bamboo, orientation, speed)
        self.is_attacking = False
        self.speed = 6
        self.sprites = {
            "idle_left": pygame.image.load("PandaPOO/Assets/Panda/panda_idle_left.png"),
            "idle_right": pygame.image.load("PandaPOO/Assets/Panda/panda_idle_right.png"),
            "up_left": pygame.image.load("PandaPOO/Assets/Panda/panda_up_left.png"),
            "up_right": pygame.image.load("PandaPOO/Assets/Panda/panda_up_right.png"),
            "down_left": pygame.image.load("PandaPOO/Assets/Panda/panda_down_left.png"),
            "down_right": pygame.image.load("PandaPOO/Assets/Panda/panda_down_right.png")
        }  
        self.current_sprite = self.sprites["idle_left"]                            
        
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
            self.y -= self.speed

    def move_down(self, y, speed):    
        if self.y < 752:
            self.y += self.speed

                             
    def die(self):  
        master.game_over()     