class Ent:  
    def __init__(self, x, y, bamboo, orientation, speed):
        self.x = x
        self.y = y 
        self.bamboo = bamboo                        
        self.orientation = orientation     
        self.speed = speed                
                                                    
    def move_up(self, y, speed):
        self.y -= self.speed
    
    def move_down(self, y, speed):
        self.y += self.speed
        
    def update_coor(self, x, bamboo, orientation):
        if self.bamboo == 1 and self.orientation == 0:
            self.x = 42
        
        elif self.bamboo == 2 and self.orientation == 0:
            self.x = 185

        elif self.bamboo == 3 and self.orientation == 0:
            self.x = 329

        elif self.bamboo == 1 and self.orientation == 1:
            self.x = 77

        elif self.bamboo == 2 and self.orientation == 1:
            self.x = 220

        elif self.bamboo == 3 and self.orientation == 1:
            self.x = 364
                
    def take_damage(self):
        pass