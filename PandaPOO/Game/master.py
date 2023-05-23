import pygame
import random
import time

class Master: 
    
    def __init__(self, score, time_passed):
        self.score = 0
        self.time_passed = int(time_passed)

    def spawn_enemy(self, enemy):
        printf("Spawn")
        
    def check_collision(self, panda, enemy):
        if panda.bamboo == enemy.bamboo and panda.orientation == enemy.orientation:
            
            if enemy.y - panda.y < 1.5:  
                panda.take_damage()
                self.game_over(self.time_passed, self.score)
                
            elif panda.y - enemy.y < 1.5:               
                enemy.take_damage()
                self.score += 1
        
    def game_over(self, time_passed, score):
        self.score = score
        self.time_passed = time_passed