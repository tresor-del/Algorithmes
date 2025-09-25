import sys

class Node():
    
    """
    Un noeud contient:
    - la position actuelle dans le lab. coord. (x, y)
    - le noeud précédent (pour reconstruire le chemin)
    - le mouvement qu'on a fait pour arriver ici
    """
    
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    """
    définition de la pile
    """
    def __init__(self):
        """La structure de donnée pile (vide ici)"""
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)
    
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty:
            raise Exception('empty frontier')
        node = self.frontier[-1] # LIFO
        self.frontier = self.frontier[:-1]
        return node

class QueueFrontier(StackFrontier):
    """
    définition de la file
    """
    def remove(self):
        if self.empty:
            raise Exception('empty frontier')
        node = self.frontier[0] # FIFO
        self.frontier = self.frontier[1:]
        return node


class Maze():

    def __init__(self, filename):

        # Lire le fichier du labyrinthe
        with open(filename) as f:
            contents = f.read()

        # valider le contenu: un seul point A et un seul point B
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Determinr la hauteur et la largeur du labyrinthe
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Définir les murs
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    # si la position a un element A, ce n'est pas un mur
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    # si la position a un element B, ce n'est pas un mur
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    # si c'est vide, ce n'est pas un mur
                    elif contents[i][j] == " ":
                        row.append(False)
                    # sinon c'est un mur 
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        # initialiser une liste pour la solution
        self.solution = None


    def print(self):
        """
        Affiche la solution 
        """
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()


    def neighbors(self, state):
        """
        cette fonction prend un etat et défini les déplacements possible
        """
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            """
            si la position de la ligne est compris entre 0 et la hauteur du maze,
            et si la colonne est compris entre 0 et la largeur du maze
            et si la position (ligne, colonne) n'est pas un mur
            on peut se déplacer
            """
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result


    def solve(self):
        """
        Cherche la solution du maze
        """

        # Ici on initialise une variable pour garder le nombre d'état déjà exploré
        self.num_explored = 0

        # Initialiser la structure de donnée, elle contient que l'état initiale 
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)
        
        # Un set vide des etats déja explorés
        self.explored = set()

        while True:

            # si la s. de d. est vide, alors pas de solution
            if frontier.empty():
                raise Exception("no solution")

            # Prendre un noeud de la s. de d. et l'ajouter au chemin explorés
            node = frontier.remove()
            self.num_explored += 1

            # Si le noeud actuel est l'objectif, alors on a la solution et onreconstruit le chemin
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # Marquer le noeud comme déjà exploré
            self.explored.add(node.state)

            # Initialiser le noeud pour la recherche suivante
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)


    def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        img.save(filename)


if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = Maze(sys.argv[1])
print("Maze:")
m.print()
print("Solving...")
m.solve()
print("States Explored:", m.num_explored)
print("Solution:") 
m.print()
m.output_image("maze.png", show_explored=True)
