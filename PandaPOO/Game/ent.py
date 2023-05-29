#Sus variables incluyen la posicion cardinal (x, y), sistema de coordenadas, y la velocidad.

class Ent:  
    def __init__(self, x, y, bamboo, orientation, speed):
        self.x = x
        self.y = y 
        self.bamboo = bamboo                        
        self.orientation = orientation     
        self.speed = speed                

    #Moverse hacia arriba (revisar linea 39 en panda.py y linea 17 en enemy.py)
    def move_up(self, y, speed):
        self.y -= self.speed
    
    #Moverse hacia abajo (revisar lineaa 43 y 46 en panda.py)
    def move_down(self, y, speed):
        self.y += self.speed
        
    #Sistema de coordenadas basado en la orientacion y en que bambu se encuentra. Segun esto, se cambia la posicion horizontal del objeto
    #(revisar linea 46 en panda.py y linea 20 en enemy.py).
    
    def update_coor(self, x, bamboo, orientation):
        if self.bamboo == 1 and self.orientation == 0:
            self.x = 51
        
        elif self.bamboo == 2 and self.orientation == 0:
            self.x = 168

        elif self.bamboo == 3 and self.orientation == 0:
            self.x = 286

        elif self.bamboo == 1 and self.orientation == 1:
            self.x = 106

        elif self.bamboo == 2 and self.orientation == 1:
            self.x = 223

        elif self.bamboo == 3 and self.orientation == 1:
            self.x = 340