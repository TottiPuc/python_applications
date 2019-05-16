import random 
from enumerar import *
class Cuarto:
	"""entidad que representa un unico cuadro del juego"""

	def __init__(self, wumpus = Estado.Ausente, hueco = Estado.Ausente, oro = Estado.Ausente):

		""" iniciamos el juego qeu por patrón es seguro y sin oro"""
		self.wumpus = wumpus
		self.hueco = hueco
		self.oro = oro

	def __str__(self):
		""" retornamos la secuencia de caracteres de cada instacia """

		return str([self.wumpus.value, self.hueco.value, self.oro.value])






class Agente:
	""" represeta el agente que recorrera el laberinto """
	def __init__(self):
		self.direccion = 1
		self.posicion = (0,0)
		self.tiene_oro = False
		self.tiene_flecha = True

	def __repr__(self):
		""" retorna la representacion dell objeto de esa instancia """
		return str([self.direccion, self.posicion, self.tiene_oro , self.tiene_flecha])

	def __str__(self):
		print("\n========================================")
		print("***** ESTADO ACTUAL DEL AGENTE ******\n")
		info = " >> localizacion: {}\n".format(self.posicion)
		info += " >> Direcion: {}\n".format(Orientacion(self.direccion).name)
		info += " >> Consiguio el Oro: {}\n".format(self.tiene_oro)
		info += " >> Aun tiene flecha: {}\n".format(self.tiene_flecha)

		return info


class Conocimiento:
	"""clase que representará el conocimiento del agente sobre el laberinto """
	def __init__(self, size=(4,4)):
		""" inicializando una nueva instancia de la clase Conocimiento"""
		self.size = size

		# En este punto el agente llega ciego no sabe nada sobre su entorno
		w,h = self.size
		estado = Estado.Desconocido, Estado.Desconocido, Estado.Desconocido
		self._cuartos = [[Cuarto(*estado) for x in range (w)] for y in range(h)] # crea una matriz con repeticiones de la clase cuarto
		#y todos estan iniciados con estado desconocido osea -1
		"""ejemplo: s = [["pol" for x in range(4)] for y in range(4)]      ó   s = [[["pol","luna"] for x in range(4)] for y in range(4)]  
		de salida [[['pol', 'luna'], ['pol', 'luna'], ['pol', 'luna'], ['pol', 'luna']],
		[['pol', 'luna'], ['pol', 'luna'], ['pol', 'luna'], ['pol', 'luna']],
		[['pol', 'luna'], ['pol', 'luna'], ['pol', 'luna'], ['pol', 'luna']],
		[['pol', 'luna'], ['pol', 'luna'], ['pol', 'luna'], ['pol', 'luna']]]"""
		 
		# cuando el agente se inicia en la pocición (0,0) se inicia en una posicion segura y sin oro
		self._cuartos[0][0] = Cuarto() # no se pasa parametros a la clase Cuarto para iniciarlo por defecto en 0 o desconocido en la pocicion [0,0]
		
	def __repr__(self):
		"""se retorna la representacion de la instancia iniciada en un string"""

		largo , alto = self.size
		planta =""
		y=0
		while y<alto:
			x=0
			while x < largo:
				planta += "{}\t".format(self._cuartos[y][x])
				x+=1
			planta += "\n" if y != alto -1 else ""
			y +=1
		return planta




class Laberinto(Conocimiento):
	""" Esta es la clase que representa el laberinto donde vive el wumpus"""
	def __init__(self, size=(4,4)):
		"""inicializa una nueva instancia de la clase Laberinto"""

		self.size = size

		# el laberinto esta formado por una matriz de cuartos de tamaño w , h
		w,h = self.size
		self._cuartos = [[Cuarto() for x in range(w)] for y in range(h)]
		peligroso = [(x,y) for x in range(w) for y in range(h) if (x,y) != (0,0)]

		# ubicación del monstruo wumpus en cualquier ubicacion del laberinto excepto la posición (0,0)

		x,y = random.choice(peligroso)
		self._cuartos[y][x].wumpus = Estado.Presente

		# ubicación del oro en el laberinto de forma aleatoria

		while True:
			x1,y1 = random.choice(peligroso)
			if (x1,y1) != (x,y):
				self._cuartos[y1][x1].oro = Estado.Presente
				break
			print("Oro ubicado en el laberinto aleatoriamente")

		# colocar los huecos en el laberinto con una probabilidad de 0.2

		for x,y in peligroso:
			if random.random() <= 0.2:
				self._cuartos[y][x].hueco = Estado.Presente

	def __repr__(self):
		"""se retorna la representacion de la instancia iniciada en un string"""

		largo , alto = self.size
		planta =""
		y=0
		while y<alto:
			x=0
			while x < largo:
				planta += "{}\t".format(self._cuartos[y][x])
				x+=1
			planta += "\n" if y != alto -1 else ""
			y +=1
		return planta


