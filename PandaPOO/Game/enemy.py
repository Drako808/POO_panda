import pygame
from ent import Ent
import time

class Enemy(Ent):
    
    def __init__(self, x, y, bamboo, orientation, speed):
        super().__init__(x, y, bamboo, orientation, speed)
        self.speed = 4
        self.sprites = {
            "left": pygame.image.load("PandaPOO/Assets/Enemy/enemy_left.png"),
            "right": pygame.image.load("PandaPOO/Assets/Enemy/enemy_right.png")
        }
        
    def move_up(self, y, speed):
        self.y += self.speed
        
    def update_coor(self, x, bamboo, orientation):
        super().update_coor(self, x, bamboo, orientation)