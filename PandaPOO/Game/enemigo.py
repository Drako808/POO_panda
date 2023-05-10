from mob import moverAbajo
import time

class enemigo:
    
    def __init__(self, direccion):
        self = self.mob
        self.direccion = direccion
        
    def die(self):
        del self
    
#Dictaminar el movimiento de los enemigos, si aparecen arriba, se
#mueven hacia abajo, y viceversa. 
    
