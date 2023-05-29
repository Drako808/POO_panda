import pygame #Se importa pygame para manejar los sprites
from ent import Ent #Se importa la superclase

#Hereda todos los atributos y metodos de Ent, pero no tiene propios.

class Enemy(Ent):
    
    def __init__(self, x, y, bamboo, orientation, speed):
        super().__init__(x, y, bamboo, orientation, speed)
        self.speed = speed
        self.sprites = { #Además de declarar las variables, se declaran los sprites y el directorio donde se encuentran.
            "left": pygame.image.load("PandaPOO/Assets/Enemy/enemy_left.png"),
            "right": pygame.image.load("PandaPOO/Assets/Enemy/enemy_right.png")
        }
        
    def move_up(self, y, speed):
        super().move_up(y, speed)
        
    def update_coor(self, x, bamboo, orientation):
        super().update_coor(x, bamboo, orientation)