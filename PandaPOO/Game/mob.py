import main

class mob:
    
    def __init__(self, posicionY, rama, posicionEnRama):
        self.posicionY = posicionY
        self.rama = rama
        self.posicionEnRama = posicionEnRama
    
    def moverArriba(self, posicionY):
        if posicionY < 100:
            posicionY += 1
    
    def moverAbajo(self, posicionY):
        if posicionY > 0:
            moverse      
            
    def recibirDano(self, posicionY, rama, posicionEnRama):
        self.die()