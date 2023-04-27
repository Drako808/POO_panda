import main

#Clase que define a los objetos principales del juego: el panda y los enemigos. 
#Se rige por cuatro parametros, tres para la posicion y uno para el movimiento

class mob:
    
    def __init__(self, posicionY, bambu, posicionEnbambu, velocidad):
        self.posicionY = posicionY                 #Posicion vertical
        self.bambu = bambu                         #En cual de los tres bambus se encuentra el objeto
        self.posicionEnbambu = posicionEnbambu     #En que lado del bambu se encuentra
        self.velocidad = velocidad                 #Que tanto se mueve por fraccion de tiempo, asi se pueden hacer enemigos con diferentes velocidades
                                                   #y replicar el movimiento de ataque del panda hacia abajo, que lo hace descender mas rapido
                                                      
    #Las funciones de movimiento delimitan al panda para que no se salga del escenario,
    #pero hace que los enemigos desaparezcan si llegan al borde
    
    def moverArriba(self, posicionY):
            if self == panda and self.posicionY < 100:
                self.posicionY += self.velocidad
                
                #Estas lineas hacen que el panda se teletransporte de vuelta al borde del escenario en caso de que lo sobrepase por un par de pixeles
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