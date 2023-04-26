from mob import mob
import random

class enemigo:
    
    def _init_(self):
        self = mob
        
    def recibir_dano(self): 
        self = 0
        
    def crear(self):
        pass     

    def spawn_enemy(min_x, max_x, min_y, max_y):
        x = random.randint(min_x, max_x)
        y = random.randint(min_y, max_y)
        enemy = Enemy( damage=10, speed=5)
        # Set the enemy's position to the random x,y location
        enemy.position = (x, y)
        return enemy