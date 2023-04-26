import main

class mob:
    
    def __init__(self, posicionY, bambu, posicionEnbambu, velocidad):
        self.posicionY = posicionY
        self.bambu = bambu
        self.posicionEnbambu = posicionEnbambu
        self.velocidad = velocidad
    
    #Las funciones de movimiento delimitan al panda para que no se salga del escenario,
    #pero hace que los enemigos desaparezcan si llegan al borde
    
    def moverArriba(self, posicionY):
            if self == panda and self.posicionY < 100:
                self.posicionY += self.velocidad
                
                #Estas lineas hacen que el panda vuelva al borde del escenario en caso de que lo sobrepase
                if self.posicionY > 100:
                    self.posicionY = 100
                
            elif self == enemigo:
                self.posicionY += self.velocidad
                if self.posicionY > 100:
                    del self
    
    def moverAbajo(self, posicionY):
            if self == panda and self.posicionY > 0:
                self.posicionY -= self.velocidad
                if self.posicionY < 0:
                    self.posicionY = 0                
                    
            elif self == enemigo:
                posicionY -= self.velocidad
                if self.posicionY < 0:
                    del self
                
    def recibirDano(self):
        self.die()