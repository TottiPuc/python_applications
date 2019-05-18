import random
from enumerar import Estado, Entidad, Acciones, Objetivo
from movimiento import vecinos, rotacion, camino_desconocido, camino_rotacion

def percibir(conoc, loc):
	""" retorna una tupla que contiene las percepciones locales del agente.
	si el agente es agarrado por el wumpus o caido en un hueco no devolvera nada"""

	if  conoc[loc].hueco == Estado.Presente or conoc[loc].wumpus == Estado.Presente:
		# el agente esta muerto o no hay percepciones
		return None

	# construir percepciones
	wumpus, hueco, oro = (Estado.Ausente,)*3

	for cuarto in [conoc[l] for l in vecinos(loc)]:

		# verificamos si el wumpus esta en este cuadro
		if cuarto.wumpus == Estado.Presente:
			wumpus = Estado.Presente
		elif cuarto.wumpus == Estado.Probable and wumpus != Estado.Presente:
			wumpus= Estado.Probable

		# verificamos si hay huecosen este cuadro
		if cuarto.hueco == Estado.Presente:
			hueco = Estado.Presente
		elif cuarto.hueco == Estado.Probable and hueco != Estado.Presente:
			hueco= Estado.Probable

	# verificamos si el oro esta en este cuarto
	if conoc[loc].oro == Estado.Presente:
		oro = Estado.Presente

	# retornamos las precepciones como una tupla
	return wumpus, hueco, oro


def tell(conoc, percepciones, loc):

  """Atualizar o conhecimento de acordo com a percepção e localização."""
  # O agente está vivo e percebeu algo assim:
  # Não há poços nem o Wumpus neste quarto
  
  conoc[loc].wumpus = conoc[loc].hueco = Estado.Ausente
  wumpus, hueco, oro = percepciones
  near = [conoc[l] for l in vecinos(loc)]
  
  # Iterar sobre quadros vecino no seguros
  for room in (r for r in near if not r.es_seguro()):
    
    # Analisar la percepcion Wumpus
    if room.wumpus != Estado.Ausente:
      if wumpus == Estado.Ausente:
        room.wumpus = Estado.Ausente
      elif wumpus == Estado.Probable:
    
        # Verificar si este es el único local donde el Wumpus puede estar
        if len([r for r in near if r.es_peligroso(Entidad.Wumpus)]) == 1:
          room.wumpus = Estado.Presente
      elif room.wumpus == Estado.Desconocido:
        if any(r.es_mortal(Entidad.Wumpus) for r in near):
    
          # el agente sabe la posicion del Wumpus -> el no puede estar en este cuadro
          room.wumpus = Estado.Ausente
        elif all(r.es_seguro(Entidad.Wumpus) for r in near if r != room):
    
          # Todos lois otros vecinos son seguros -> el Wumpus debe estar en este cuadro
          room.wumpus = Estado.Presente
        else:
          room.wumpus = Estado.Probable
    
    # Analisar la percepcion de los huecos
    if room.hueco != Estado.Ausente:
      if hueco == Estado.Ausente:
        room.hueco = Estado.Ausente
      elif hueco == Estado.Probable:
        
        # Verifique se este es el único lugar donde el hueco puede estar
        if len([r for r in near if r.es_peligroso(Entidad.hueco)]) == 1:
          room.hueco = Estado.Presente
      elif room.hueco == Estado.Desconocido:
        if all(r.es_seguro(Entidad.hueco) for r in near if r != room):
        
          # Todos lois otros vecinos son seguros -> el hueco debe estar en este cuadro
          room.hueco = Estado.Presente
        else:
          room.hueco = Estado.Probable
  
  # Analisa la percepcion del ouro
  conoc[loc].oro = oro

def actualizar(conoc, loc):
  
  """Atualizar el conocimiento."""
  # Atualiza el conocimento de acuerdo con todos los cuadros ya explorados
  
  for l in [x for x in conoc.explorada]:
    tell(conoc, percibir(conoc, l), l)


def preguntar(kb, loc, direction, goal):
  
  """Retorna una accion de acuerdo con el estado actual del conocimiento.
  la accion es una tupla: el primer elemento es el tipo de accion
  el segundo elemento es una lista de movimiento se el tipo es Acciones.Moverr o disparar
  y el tercer (caso contrario), es None"""
  
  # Si el agente está buscando oro

  if goal == Objetivo.Buscar:
    
    # Verifica se esta sala contiene oro
    if kb[loc].oro == Estado.Presente:
      return Objetivo.Coger, None
    
    # Obtiene le primer cuadro vecino seguro e inexplorado (si es que existe)
    state = lambda r: r.es_seguro() and r.es_inexplorada
    dest = next((l for l in vecinos(loc) if state(kb[l])), None)
    if dest:
      return Acciones.Moverse, (rotacion(loc, direction, dest),)
    
    # Obtiene cualquier cuadro seguro e inesperado (si el agente puede alcanzarlo)
    state = lambda r, l: r.es_seguro() and any(kb[x].es_explorada for x in vecinos(l))
    dest = next((l for l in kb.inexplorada if state(kb[l], l)), None)
    if dest:
      path = camino_desconocido(kb, loc, dest)
      return Acciones.Moverse, camino_rotacion(path, direction)
    
    # Obtém un cuadro vecino que puede tener al wumpus pero no un hueco
    state = lambda r: r.es_seguro(Entidad.hueco) and r.es_inseguro(Entidad.Wumpus)
    dest = next((l for l in vecinos(loc) if state(kb[l])), None)
    if dest:
      return Acciones.Disparar, rotacion(loc, direction, dest)
    
    # Obtém un cuadro vecino que puede tener al wumpus pero no un hueco
    state = lambda r: r.es_seguro(Entidad.hueco) and r.es_inseguro(Entidad.Wumpus)
    dest = next((l for l in kb.inexplorada if state(kb[l])), None)
    if dest:
    
      # Obtiene un cuadro vecino esplorado
      dest = next((l for l in vecinos(dest) if kb[l].es_explorada))
      path = camino_desconocido(kb, loc, dest)
      return Acciones.Moverse, path_to_rotacion(path, direction)
    
    # Obtiene un cuadro vecino quqe puede tener al Wumpus
    state = lambda r: r.es_peligroso(Entidad.Wumpus)
    dest = next((l for l in vecinos(loc) if state(kb[l])), None)
    if dest:
      return Acciones.Disparar, rotacion(loc, direction, dest)
    
    # Obtiene un cuadaro vecino que puede tener un hueco
    rooms = [l for l in kb.inexplorada if kb[l].es_peligroso(Entidad.hueco)]
    if rooms:
      dest = random.choice(rooms)
      path = camino_desconocido(kb, loc, dest)
      return Acciones.Moverse, camino_rotacion(path, direction)
    
    # Obtiene un cuadro explorado
    dest = next((l for l in kb.inexplorada), None)
    if dest:
      path = camino_desconocido(kb, loc, dest)
      return Acciones.Moverse, camino_rotacion(path, direction)

  
  # Incapaz de encontrar una accion
  return None
