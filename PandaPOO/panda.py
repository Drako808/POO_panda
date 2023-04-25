from mob import mob
from enemigo import enemigo

class panda:

    def _init_(self, vida, atancando):   
        self = mob
        self.vida = 3
        atacando = bool = False

    #Funcion de recibir daño
    if self.rama == enemigo.rama and self.posicionEnRama == enemigo.posicionEnRama:
        
        #Recibir daño desde abajo
        
        if self.posicionY > enemigo.posicionY and atacanco is False:
            if self.posicionY - enemigo.posicionY > 0.3:
                self.vida -= 1      
                
        #Recibir daño desde arriba        
               
        if self.posicionY < enemigo.posicionY:
            if enemigo.posicionY - self.posicionY > 0.3:
                self.vida -= 1                               
            
    #Funcion de morir                        
    if self.vida == 0:
        print("Has sido derrotado.")
        self = 0      
        
    def moverArriba(self, posicionY):
        posicionY += 1
        
    def moverAbajo(self, posicionY):
        posicionY -= 1
        
    def moverIzquierda(self, rama, posicionEnRama):
        if rama != 1 and rama == 0:       
            rama -= 1
            
        if posicionEnRama == 1:
            posicionEnRama = 0
    
    def moverDerecha(self, rama, posicionEnRama):     
        if rama != 3 and rama == 1:       
            rama += 1
            
        if posicionEnRama == 0:
            posicionEnRama = 1
                        
    def atacar(self, enemigo, posicionY):
        atacando = True
        posicionY -= 1.5
        if posicionY == posicionY.enemigo + 0.3:
            enemigo(recibir_dano)        