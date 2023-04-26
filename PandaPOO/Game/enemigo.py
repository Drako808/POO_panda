import mob
import time

class enemigo:
    
    def __init__(self, direccion):
        self = mob
        self.direccion = direccion
        
    def die(self):
        main.score += 1
        del self
    
#Dictaminar el movimiento de los enemigos, si aparecen arriba, se
#mueven hacia abajo, y viceversa. 
    
while Playing is True:
    self.velocidad = 3
    if self.direccion == 0:
        moverArriba()
        time.sleep(0.2)
    if self.direccion == 1:
        moverAbajo()
        time.sleep(0.2)