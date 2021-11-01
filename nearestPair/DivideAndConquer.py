import math
import copy
import time

#Una clase para representar un punto en plano 2D
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

# Una función útil para encontrar la distancia de 2 puntos(Pitágoras)
def dist(p1, p2):
	return math.sqrt((p1.x - p2.x) **2 +(p1.y - p2.y) **2)

# Método de fuerza bruta, devuelve
# la distancia mas pequeña entre dos puntos en P[] de tamaño n(entradas)
def bruteForce(P, n):
	min_val = math.inf
	for i in range(n):
		for j in range(i + 1, n):
			if dist(P[i], P[j]) < min_val:
				min_val = dist(P[i], P[j])

	return min_val

# Función de utilidad para encontrar la distancia mas cercana entre dos puntos
# de un arreglo de tamaño n. Debemos organizar todos los puntos de acuerdo
# a la coordenada y. Todos los puntos tienen un límite superior de dist d
def stripClosest(strip, size, d):
	
	# Inicio la distancia mínima como d
	min_val = d
    #Con este loop trato todas las distancias de la coordenada y
    #hasta hallar la dist mínima entre y & d
	for i in range(size):
		j = i + 1
		while j < size and (strip[j].y -
							strip[i].y) < min_val:
			min_val = dist(strip[i], strip[j])
			j += 1

	return min_val

#Esta es mi función recursiva para encontrar la dist más pequeña, en
#esta ocasión el array contiene todos los puntos organizados de acuerdo
#a la coordenada x
def closestUtil(P, Q, n):
	
	# Si hay 2 o 3 puntos lo mejor es usar fuerza bruta(bruteForce)
	if n <= 3:
		return bruteForce(P, n)

	# para encontrar la mitad del punto
	mid = n // 2
	midPoint = P[mid]

	#Con estos slices, mantengo una copia de la rebanada de la izq y una de la derecha
	Pl = P[:mid]
	Pr = P[mid:]

    #dl la distacia desde el punto medio al cuadrante izquierdo
    #dr la distancia desde el punto medio al cuadrante derecho
	dl = closestUtil(Pl, Q, mid)
	dr = closestUtil(Pr, Q, n - mid)

	# Encontrar la distancia mas corta de ambas
	d = min(dl, dr)

	#Creo un array llamado strip con puntos mas cercanos que d
	stripP = []
	stripQ = []
	lr = Pl + Pr
	for i in range(n):
		if abs(lr[i].x - midPoint.x) < d:
			stripP.append(lr[i])
		if abs(Q[i].x - midPoint.x) < d:
			stripQ.append(Q[i])

	stripP.sort(key = lambda point: point.y) 
	min_a = min(d, stripClosest(stripP, len(stripP), d))
	min_b = min(d, stripClosest(stripQ, len(stripQ), d))
	return min(min_a,min_b)


# La librería copy me permite insertar datos recursivamente
def closest(P, n):
	P.sort(key = lambda point: point.x)
	Q = copy.deepcopy(P)
	Q.sort(key = lambda point: point.y)

	# Use recursivamente la funcion closesUtil()
	# para encontrar la distancia mas pequeña.
	return closestUtil(P, Q, n)


P = [Point(2, 3), Point(12, 30),
     Point(40, 50), Point(5, 1),
     Point(12, 10), Point(3, 4)]
n = len(P)
start = time.time()
pair = closest(P, n)
end = time.time()
print(end - start)
print(f'The closest point is: {pair}')



# Código creado por Simón López
# Libro de apoyo "Introduction to Algorithms" by Thomas Cormen, 
# Charles Leiserson, Ronald Rivest and Clifford Stein.
