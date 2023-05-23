import random
import time
from enemy import Enemy

class Master: 
    
    def __init__(self, score, time_passed):
        self.score = 0
        self.time_passed = int(time_passed)

    def spawn_enemy(self, enemy):
        x = 0
        y = 840
        bamboo = random.randint(1, 3)
        orientation = random.randint(0, 1)
        speed = random.randint(1, 5)
        return Enemy(x, y, bamboo, orientation, speed)

        
    def check_collision(self, panda, enemy):
        if panda.bamboo == enemy.bamboo and panda.orientation == enemy.orientation:
            
            if enemy.y - panda.y < 1.5:  
                panda.take_damage()
                self.game_over(self.time_passed, self.score)
                
            elif panda.y - enemy.y < 1.5:               
                enemy.take_damage()
                self.score += 1
        