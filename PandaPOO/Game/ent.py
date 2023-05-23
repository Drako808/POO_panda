import pygame

class Ent:  
    def __init__(self, x, y, bamboo, orientation, speed):
        self.x = x
        self.y = y 
        self.bamboo = bamboo                        
        self.orientation = orientation     
        self.speed = speed                
                                                    

    
    def move_up(self, y):
        pass
    
    def move_down(self, y):
        pass
                
    def take_damage(self):
        pass