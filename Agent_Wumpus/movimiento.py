#! /usr/bin/env python


# Módulo que define los movimientos del agente

# el objeto delta usado para mover al agente y alcanzar  los vecinos
DELTA = (0, -1), (1, 0), (0, 1), (-1, 0)


def vecinos(posicion, size=(4, 4)):
  
  """Retorna un generador para los cuadros vecinos."""
  
  x, y = posicion
  ancho, alto = size
  
  #  cuadro de encima
  if y - 1 >= 0:
    yield x, y - 1
  
  # cuadro de la derecha
  if x + 1 < ancho:
    yield x + 1, y
  
  # cuadro de abajo
  if y + 1 < alto:
    yield x, y + 1
  
  # cuadro de la izquierda
  if x - 1 >= 0:
    yield x - 1, y


def vecino(posicion, direccion, size=(4, 4)):
  
  """Obtener un vezino de aceurdo con la posicion y su direccion."""
  
  x, y = posicion
  ancho, alto = size
  dx, dy = DELTA[direccion]
  
  # Verifica si el vecino esta dentro del laberinto
  if 0 <= x + dx < ancho and 0 <= y + dy < alto:
    return x + dx, y + dy


def girar(direccion, steps):
  
  """Retorna la nueva direccion."""
  print ((direccion + steps) % len(DELTA))
  return (direccion + steps) % len(DELTA)


def mover_adelante(posicion, direccion):
  
  """Retorna una nueva posicion."""
  
  return vecino(posicion, direccion)


def rotacion(source, direccion, destino):

  """Obtiene el numero de rotaciones necesaria para tener el cuadro de destino al frente."""

  assert source in vecinos(destino)
  
  # Calcula la diferencia entre los cuadros
  diff = tuple([a - b for a, b in zip(destino, source)])
  rot = DELTA.index(diff) - direccion
  rot = rot if rot != 3 else -1
  
  # Retorna el numeor minimo de rotaciones  (sentido horário vs sentido anti-horário)
  return rot


def camino_desconocido_rec(kb, loc, dest, camino, visitado):

  """Algoritmo de Busqueda: Busca en profundidad  y construye un camino explorado para el destino."""

  if loc == dest:
    return True
  
  # Generador de vecinos explorados (pero aun no visitados por la busqueda)
  vecindario = (l for l in vecinos(loc) if l not in visitado 
                  and (kb[l].is_explored or l == dest))
  
  # Iterar sobre cada vecino
  for n in vecindario:
    
    # Adicionar el nodo al camino
    camino.append(n)
    visitado.add(n)
    
    # llamada recursiva
    if known_path_rec(kb, n, dest, camino, visitado):
      return True
    
    # Backtrack: este nodo no conduce al destino
    visitado.remove(n)
    camino.remove(n)
  return False


def camino_desconocido(conoc, loc, dest):
  
  """Retorna un camino explorado para el destino."""
  
  camino = [loc]
  visitado = set()
  visitado.add(loc)
  
  # Retorna el camino o ningun camino en caso de no ser encontrado 
  if camino_desconocido_rec(conoc, loc, dest, camino, visitado):
    return tuple(camino)


def camino_rotacion(camino, direccion):
  
  """Obtenemos una lista de rotaciones que el agente debe ejecutar para seguir el camino."""
  
  # Verifica la presencia de un camino valido
  assert camino is not None
  rotaciones = []
  
  # Sigue el camino y calcula los pasos necesários para girar y despues avanzar
  # hasta alzanzar la ultima posicion del camino 
  i = 0
  while i < len(camino) - 1:
    rot = rotacion(camino[i], direccion, camino[i + 1])
    rotaciones.append(rot)
    direccion = (direccion + rot) % len(DELTA)
    i += 1
  return tuple(rotaciones)
