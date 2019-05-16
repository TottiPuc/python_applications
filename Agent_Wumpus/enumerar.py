""" definicion de estados para la matrix 4x4"""

from enum import Enum

class Estado(Enum):
	""" Creamos atributos de clase para enumerar e indicar el estado de cada cuadro """
	Desconocido = -1
	Ausente = 0
	Presente = 1
	Probable = 2


class Entidad(Enum):
	""" Creamos atributos de clase para enumerar e indicar los estados de cada entidad presente en el juego( wumpus, hueco, oro)"""
	Wumpus = 0
	hueco = 1
	Oro = 2


class Acciones(Enum):
	""" Creamos atributos de clase para enumerar e indicar el estado de las acciones que realizara el agente ( moverse, disparar, coger, girar) """
	Moverse = 1
	Disparar = 2
	Coger = 3
	Girar = 4


class Objetivo(Enum):
	""" creamos atributos de clase para enumerar e indicar los objetivos del agente (buscar Oro, volver a la entrada)"""
	Buscar =0
	Vovler =1


class Orientacion(Enum):
	""" enumeramos las posibles orientaciones que puede tomar el agente( norte, sur, este, oeste)"""
	Norte = 1
	Sur =2
	Este = 3
	Oeste = 4
