import random
import itertools
import collections
import time

class Node:
    """
   La clase representa un nodo de resolución:
    - 'puzzle' es una instancia del puzzle
    - 'parent' Nodo anterior generado por el solucionador, si hay
    - 'action' Es la acción tomada para producir el puzzle, si hay
    """
    def __init__(self, puzzle, parent=None, action=None):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        if (self.parent != None):
            self.g = parent.g + 1
        else:
            self.g = 0

    
    """Una función para representar el coste de g + h"""
    @property
    def score(self):
        return (self.g + self.h)

    """Estado del puzzle"""    

    @property
    def state(self):
        
        return str(self)

    """
        Reconstruye la ruta desde la raíz padre
    """    
    @property 
    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    @property
    def solved(self):
        """ comprobar si el puzzle esta solucionado"""
        return self.puzzle.solved

    @property
    def actions(self):
        """Estado actual de las posibles acciones """
        return self.puzzle.actions

    @property
    def h(self):
        """"h"""
        return self.puzzle.manhattan

    @property
    def f(self):
        """"f"""
        return self.h + self.g

    def __str__(self):
        return str(self.puzzle)


# clase solución
class Solver:
    """
    Solucionador para'puzzle-8'
    - 'start' es una instancia de inicio del puzzle
    """
    def __init__(self, start):
        self.start = start

    def solve(self):
        """
        Realiza la búsqueda en amplitud y devuelve una ruta
        si la encuentra.
        """
        queue = collections.deque([Node(self.start)])
        seen = set()
        seen.add(queue[0].state)
        while queue:
            queue = collections.deque(sorted(list(queue), key=lambda node: node.f))
            node = queue.popleft()
            if node.solved:
                return node.path

            for move, action in node.actions:
                child = Node(move(), node, action)

                if child.state not in seen:
                    queue.appendleft(child)
                    seen.add(child.state)       

#clase puzzle
class Puzzle:
    """
    Esta clase representa un tablero de puzzle-8.
    - 'board' debe ser una lista cuadrada de listas con enteros entre 0...ancho^2 - 1
       ejemplo [[1,2,3],[4,0,6],[7,5,8]]
    """
    def __init__(self, board):
        self.width = len(board[0])
        self.board = board

    @property
    def solved(self):
        """
        El puzzle es resuelto si los numeros del tablero son
        crecientes en orden de izq a derecha y el '0' esta en el 
        ultimo recuadro de esa lista creciente.
        
        """
        N = self.width * self.width
        return str(self) == ''.join(map(str, range(1,N))) + '0'

    @property 
    def actions(self):
        """
        Devuelve una lista de 'move', 'action' pairs. 'move' puede ser llamado
        para obtener un nuevo puzzle que resulta en un deslizamiento del '0' en la
        dirección de 'action'.
        """
        def create_move(at, to):
            return lambda: self._move(at, to)

        moves = []
        for i, j in itertools.product(range(self.width),
                                      range(self.width)):
            direcs = {'R':(i, j-1),
                      'L':(i, j+1),
                      'D':(i-1, j),
                      'U':(i+1, j)}

            for action, (r, c) in direcs.items():
                if r >= 0 and c >= 0 and r < self.width and c < self.width and \
                   self.board[r][c] == 0:
                    move = create_move((i,j), (r,c)), action
                    moves.append(move)
        return moves

    @property
    def manhattan(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j]-1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def shuffle(self):
        """
        Devuelve un nuevo puzzle que ha sido barajeado o mezclado con 1000 movimientos 
        aleatorios
        """
        puzzle = self
        for _ in range(1000):
            puzzle = random.choice(puzzle.actions)[0]()
        return puzzle

    def copy(self):
        """
        Devuelve un nuevo puzzle con el mismo tablero tablero 'board' como 'self'
        """
        board = []
        for row in self.board:
            board.append([x for x in row])
        return Puzzle(board)

    def _move(self, at, to):
        """
        Retorna un nuevo puzzle donde 'at'(en) y 'to'(para)han sido los movimientos realizados.
        NOTE: Todos los movimientos deben ser 'actions' que han sido ejecutadas.
        """
        copy = self.copy()
        i, j = at
        r, c = to
        copy.board[i][j], copy.board[r][c] = copy.board[r][c], copy.board[i][j]
        return copy

    def pprint(self):
        for row in self.board:
            print(row)
        print()

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.board:
            yield from row     

# Ejemplo de uso
board = [[1,2,3],[4,5,0],[6,7,8]]
puzzle = Puzzle(board)
s = Solver(puzzle)
tic = time.time()
p = s.solve()
toc = time.time()

steps = 0
for node in p:
    print(node.action)
    node.puzzle.pprint()
    steps += 1

print("Total numero de pasos: " + str(steps))
print("Total valor de tiempo de solución: " + str(toc - tic) + " second(s)")                           