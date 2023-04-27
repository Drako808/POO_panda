import main
import mob
import enemigo

class panda:

    def __init__(self, atacando):   
        self = mob
        self.atacando = bool(False)                                
        
    #Las funciones de movimiento horizontal del panda le permiten moverse a un lado u otro del bambu, o moverse entre bambus,
    #pero no puede moverse a, por ejemplo, la derecha, si ya esta en el bambu de la derecha (izquierda = 1, centro = 2, derecha = 3)
        
    def moverIzquierda(bambu, posicionEnbambu):
        if self.bambu != 1 and self.bambu == 0:       
            self.bambu -= 1
            
        if self.posicionEnbambu == 1:
            self.posicionEnbambu = 0
    
    def moverDerecha(bambu, posicionEnbambu):     
        if self.bambu != 3 and self.posicionEnbambu == 1:       
            self.bambu += 1
            
        if posicionEnbambu == 0:
            posicionEnbambu = 1
                        
    def atacar(self, enemigo, posicionY, velocidad):
        atacando = True
        velocidad = 4.5
        moverAbajo()
        if self.posicionY == posicionY.enemigo + 0.9:
            enemigo.recibir_dano()        
               
    #Recibir daño desde arriba 
                          
    if self.bambu == enemigo.bambu and self.posicionEnbambu == enemigo.PosicionEnbambu:
        if enemigo.posicionY - self.posicionY < 1.5: 
            self.recibirDano() 

    #Recibir daño desde abajo, excepto si se esta realizando un ataque          
         
    while self.bambu == enemigo.bambu and self.posicionEnbambu == enemigo.PosicionEnbambu and atacando is False:
        if self.posicionY - enemigo.posicionY < 1.5: 
            self.recibirDano() 
            
    def die(self):  
        main.gameOver()     