from mob import mob
import random

class enemigo:
    
    def _init_(self):
        self = mob
        
    def crear(posicionY, posicionEnRama, rama):
        posicionY = random.randint(0, 100)
        posicionEnRama = random.randint(1, 3)
        rama = random.randint(0, 1)