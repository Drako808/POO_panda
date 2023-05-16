from mob import moverAbajo
import time

class enemigo(Mob):
    
    def __init__(self):
        super().__init__(posicionY, bambu, posicionEnBambu, velocidad)
        
    def die(self):
        del self
    if time.time() < 30:
        self.velocidad = 100
    elif time.time() < 60:
        self.velocidad = 100 - ((time.time() - 30) / 5)
