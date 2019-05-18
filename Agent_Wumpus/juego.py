import sys
import random
from entidades import *
from conocimiento import *
from movimiento import *




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

def print_percepcion(percepciones):
	wumpus, hueco, oro = percepciones
	if wumpus == Estado.Presente:
		print('Ud sintio un escalofrio el wumpus esta cerca.')
	if hueco == Estado.Presente:
		print('Ud sintio una brisa hay un hueco cerca.')
	if oro == Estado.Presente:
		print('Ud miro el oro brillar, esta cerca.')
	if percepciones == (Estado.Ausente,)*3:
		print('Ud no ha percibido nada')
	print()

def convertir_accion(accion):
	if accion ==1:
		return Acciones.Moverse, (0,)
	elif accion == 2:
		return Acciones.Girar, -1
	elif accion == 3:
		return Acciones.Girar, 1
	elif accion == 4:
		return Acciones.Coger, None
	elif accion == 5:
		return Acciones.Disparar, None
    





if __name__ == "__main__":

	# damos la bienvenida al juego
	bienvenida()
	
#===========================================================================================
	#Definimos los objetos o  entidades ( Agente, Laberinto y Conocimiento)
	agente =  Agente()
	#print(agente)
	conocimiento = Conocimiento()
	#print(conocimiento)
	laberinto = Laberinto()
	print(laberinto) # solución muestra en que parte se encuentra el wumpus el oro y los huecos 
#===========================================================================================
	
while True:
	print("Agente:\n {}".format(agente))
	dibujar(agente.posicion)
	

	# percepcion en el cuadro actual
	percepciones = percibir(laberinto, agente.posicion)
	if percepciones is None:
		print("Fin del juego XXX Acaba de morir XXX")
		break

	print_percepcion(percepciones)

	# Activar el modulo de inteligencia artificial pasando como parametro de entrada -Inteligencia

	if "-Inteligencia" in sys.argv:
		pass
	else:
		# presentam las instrucciones del juego 
		movimientos()
		accion = int(input("Qual es su proximo movimiento! "))
		print()
		accion = convertir_accion(accion)
		print (convertir_accion)

	# realizar acciones
	if agente.rendimiento (accion, laberinto, conocimiento):
		print ("Usted escucho un gruñido. \n")

	if agente.tiene_oro and agente.posicion == (0,0):
		dibujar(agente.posicion)
		print("Usted derroto al wumpus y gano el juego .I.")
		break
