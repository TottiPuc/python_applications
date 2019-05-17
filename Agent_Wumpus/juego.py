import sys
import random
from entidades import *




def bienvenida():
	print ("\n")
	print ("==========================================")
	print ("| Bienvenido al mundo de wumpus           |")
	print ("| Aplicación de inteligencia artificial   |")
	print ("==========================================")
	print ("\n")


def movimientos():
	print (" Instrucciones de juego oprima un número \n")
	print (" 1) Mover para adelante")
	print (" 2) Mover para la izquierda")
	print (" 3) Mover para la derecha")
	print (" 4) Tomar el oro")
	print (" 5) Disparar la flecha")

def dibujar(loc):
	print ( "\n que empiece el juego \n")
	print ("____________________")
	y=0
	while y < 4:
		x=0
		while x < 4:
			print ("|_X_|" if (x,y) == loc else "|___|", end="")
			x +=1
		print()
		y +=1
	print()




if __name__ == "__main__":

	# damos la bienvenida al juego
	bienvenida()
	# presentam las instrucciones del juego 
	movimientos()

#===========================================================================================
	#Definimos los objetos o  entidades ( Agente, Laberinto y Conocimiento)
	agente =  Agente()
	#print(agente)
	conocimiento = Conocimiento()
	#print(conocimiento)
	laberinto = Laberinto()
	#print(laberinto) # solución muestra en que parte se encuentra el wumpus el oro y los huecos 
#===========================================================================================
	


	dibujar((1,3))

