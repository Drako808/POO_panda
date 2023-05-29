import random
import time #Modulo de python que permite exportar funciones de tiempo del sistema.
from enemy import Enemy #Modulo de enemigos para controlar su creacion.

class Master: 
    
    #Sus variables incluyen el tiempo y el puntaje (revisar lineas 115-117 en main.py).
    
    def __init__(self, score, time_passed): 
        self.score = 0
        self.time_passed = int(time_passed)


    #Crear enemigos con instancias aleatorias de posicion -excepto vertical- y de velocidad (revisar linea 123 en main.py).
    
    def spawn_enemy(self, enemy):
        x = 0
        y = 840
        bamboo = random.randint(1, 3)
        orientation = random.randint(0, 1)
        speed = random.randint(1, 8)
        return Enemy(x, y, bamboo, orientation, speed)        