from mob import mob
from enemigo import enemigo

class panda:

    def _init_(self, atacando):   
        self = mob
        atacando = bool = False                            
            
    #Funcion de morir                        
    if vida == 0:
        print("Has sido derrotado.")
        self = 0      
        
    def moverIzquierda(rama, posicionEnRama):
        if rama != 1 and rama == 0:       
            rama -= 1
            
        if posicionEnRama == 1:
            posicionEnRama = 0
    
    def moverDerecha(rama, posicionEnRama):     
        if rama != 3 and posicionEnRama == 1:       
            rama += 1
            
        if posicionEnRama == 0:
            posicionEnRama = 1
                        
    def atacar(self, enemigo, posicionY):
        atacando = True
        posicionY -= 1.5
        if self.posicionY == posicionY.enemigo + 0.3:
            enemigo(recibir_dano)        