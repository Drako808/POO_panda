from PandaPOO.Game import mob, enemigo, panda
import random
import time

#Clase principal que controla el juego y sus funciones principales, como manejar el puntaje o la creacion de enemigos

class master: 
    
    def __init__(self, score, highScore, tiempo, highTime):
        self.score = int(0)
        self.highScore = int(0)
        self.time = int(0)
        self.highTime = int(0)
        
    def crearEnemigo():
        #Parametros de posicion inicial del enemigo
        enemigo.posicionY = random.randint(0 or 100)   #Si aparece arriba o abajo del escenario
        enemigo.posicionEnbambu = random.randint(1, 3) #En cual de los tres bambus aparece 
        enemigo.bambu = random.randint(1, 2)           #En que lado del bambu aparece
        
        #Si aparece hacia arriba, mirara hacia abajo, y viceversa
        if enemigo.posicionY == 0:
            enemigo.direccion = 0
        if enemigo.posicionY == 100:
            enemigo.direccion = 1
        
    #Cuando el jugador muere, se guarda el record de puntuacion y de tiempo en caso de que lo haya y se reinicia el escenario
    def gameOver(score, highScore, tiempo, highTime):
        
        if score > highScore:
        
            highScore = score
        if time > highTime:
            highTime = time
            
            
        score = 0