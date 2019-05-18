import random 
from enumerar import Entidad, Estado, Acciones, Objetivo, Orientacion
from movimiento import *
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

	def es_seguro(self, peligro=None):
		""" devolvera un True si en el cuadro actual no hay ni un hueco ni el wumpus"""
		if peligro is None:
			return self.wumpus == Estado.Ausente and self.hueco == Estado.Ausente
		if peligro == Entidad.Wumpus:
			return self.wumpus == Estado.Ausente
		if peligro == Entidad.hueco:
			return self.hueco == Estado.Ausente
		raise ValueError

	def es_inseguro(self, peligro=None):
		"""devuelve True si el cuadro no tiene ni wunpus ni hueco"""
		return self.es_peligroso(peligro) or self.es_mortal(peligro)

	def es_peligroso(self, peligro=None):
		""" devolvera True si en el cuadro puede existir presencia del wumpus o haber un hueco """
		if peligro is None:
			return self.wumpus == Estado.Probable and self.hueco == Estado.Probable
		if peligro == Entidad.Wumpus:
			return self.wumpus == Estado.Probable
		if peligro == Entidad.hueco:
			return self.hueco == Estado.Probable
		raise ValueError


	def es_mortal(self, peligro=None):
		"""  devuelve True si en el cuadro definitivamente hay Wumpus o un hueco """
		if peligro is None:
			return self.wumpus == Estado.Presente and self.hueco == Estado.Presente
		if peligro == Entidad.Wumpus:
			return self.wumpus == Estado.Presente
		if peligro == Entidad.hueco:
			return self.hueco == Estado.Presente
		raise ValueError

	@property
	def es_explorada(self):
		""" devuelve True si la sala ya fue explorada"""
		assert self.oro != Estado.Probable
		return self.oro != Estado.Desconocido

	@property
	def es_inexplorada(self):
		""" devuelve un True si la sala no fue inexplorada"""
		return self.es_explorada
	
		
	

class Agente:
	""" represeta el agente que recorrera el laberinto """
	def __init__(self):
		self.posicion = (0,0)
		self.direccion = 1
		self.tiene_oro = False
		self.tiene_flecha = True

	def __repr__(self):
		""" retorna la representacion dell objeto de esa instancia """
		return str([self.posicion, self.direccion,  self.tiene_oro , self.tiene_flecha])

	def __str__(self):
		print("\n========================================")
		print("***** ESTADO ACTUAL DEL AGENTE ******\n")
		info = " >> localizacion: {}\n".format(self.posicion)
		info += " >> Direcion: {}\n".format(Orientacion(self.direccion).name)
		info += " >> Consiguio el Oro: {}\n".format(self.tiene_oro)
		info += " >> Aun tiene flecha: {}\n".format(self.tiene_flecha)

		return info

	def rendimiento(self, accion, labe, conoc):
		""" ejecutara una acción. la cual retornara True si la acción mata al wumpus si no retornara falso"""
		tipo, rotacion = accion
		if tipo == Acciones.Moverse:
			self.mover(rotacion)
		elif tipo == Acciones.Disparar:
			if rotacion is not None:
				self.direccion = girar(self.direccion, rotacion)
			return self.disparar(labe,conoc)
		elif tipo == Acciones.Coger:
			labe[self.posicion].gold = Estado.Ausente
			self.tiene_oro = True
		elif tipo == Acciones.Girar:
			self.direccion = girar(self.direccion, rotacion)
		return False

	def mover(self, rotacion):
		"""funcion que mueve al agente """
		for steps in rotacion:
			self.direccion = girar(self.direccion, steps)
			self.posicion = mover_adelante(self.posicion, self.direccion )


	def disparar(self, labe, conoc):
		""" lanzara la flecha y verifica si el wumpus fue herido """
		x,y = self.posicion
		ancho, alto = labe.size

		# retirar la flecha
		self.tiene_flecha= False

		# dispara de acuerdo con la direccion acutal """
		if self.direccion == 0:

			# sigue los cuadros de arriba
			i = y
			while i >=0:
				conoc[x,i].wumpus = Estado.Ausente
				if labe[x,i].wumpus == Estado.Presente:
					labe[x,i].wumpus = Estado.Ausente
					conoc.matar_wumpus()
					return True
				i +=1
		elif self.direccion == 1:

			# sigue los cuadros de la derecha
			i = x
			while i <ancho:
				conoc[i,y].wumpus = Estado.Ausente
				if labe[i,y].wumpus == Estado.Presente:
					labe[i,y].wumpus = Estado.Ausente
					conoc.matar_wumpus()
					return True
				i +=1
		if self.direccion == 2:

			# sigue los cuadros de abajo
			i = y
			while i < alto:
				conoc[x,i].wumpus = Estado.Ausente
				if labe[x,i].wumpus == Estado.Presente:
					labe[x,i].wumpus = Estado.Ausente
					conoc.matar_wumpus()
					return True
				i +=1
		else:
			# sigue los cuadros de la izquierda
			i = x
			while i >= 0:
				conoc[i,y].wumpus = Estado.Ausente
				if labe[i,y].wumpus == Estado.Presente:
					labe[i,y].wumpus = Estado.Ausente
					conoc.matar_wumpus()
					return True
				i +=1
		# si la flecha no mata al wumpus
		return False




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

	def __getitem__(self,posicion):
		""" obtiene el punto exacto del agente"""
		x,y = posicion
		#print(x,y)
	
		return self._cuartos[y][x]

	def __setitem__(self, posicion, value):
		""" define la direccion en el cuarto del agente"""
		x,y = posicion
		self._cuartos[y][x] = value

	def cuartos (self, condicion=None):
		""" retorna un generador de indices de cada cuadro que cumple con las condiciones"""

		y=0
		for path in self._cuartos:
			x=0
			for cuarto in path:
				if condicion is None or condicion(cuarto):
					yield x,y
				x+=1
			y+=1

	@property
	def explorada(self):
		"""retorna un explorador de indices de los cuadros ya explorados"""
		return self.cuartos(lambda r: r.es_explorada)

	@property
	def inexplorada(self):
		return self.cuartos(lambda r: not r.es_explorada)

	def matar_wumpus(self):
		"""altera el estado de cada cuadro de tal manera que no puede ser el wumpus"""
		for path in self._cuartos:
			for cuarto in path:
				cuarto.wumpus = Estado.Ausente
	

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


