import Game
import random
import time

class game: 
    
    def __init__(self, score, highScore, time, highTime):
        self.score = int(0)
        self.highScore = int(0)
        self.time = int(0)
        self.highTime = int(0)
        
    def crearEnemigo():
        enemigo.posicionY = random.randint(0, 100)
        enemigo.posicionEnRama = random.randint(1, 3)
        enemigo.rama = random.randint(0, 1)
        

    def gameOver(self, score, highScore, time, highTime):
        
        del panda
        del enemigo



#Calculo para recibir daño
if panda.rama == enemigo.rama and panda.posicionEnRama == enemigo.posicionEnRama:
    panda(recibir_dano)
