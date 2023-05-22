import pygame
from ent import Ent
import time

class Enemy(Ent):
    
    def __init__(self, y, bamboo, orientation, speed):
        super().__init__(y, bamboo, orientation, speed)
        self.speed = 25
        self.sprites = {
            "enemy.left": pygame.image.load("PandaPOO/Assets/Enemy/enemy_left.png"),
            "enemy.right": pygame.image.load("PandaPOO/Assets/Enemy/enemy_right.png")
        }
        

