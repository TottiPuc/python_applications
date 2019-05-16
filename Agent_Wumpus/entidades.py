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
