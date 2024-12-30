# puzzle.py

from aima.search import Problem, Node, breadth_first_tree_search, depth_first_tree_search, uniform_cost_search, astar_search
import sys

class PuzzleProblem(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        # Définir les actions possibles (mouvements glissants)
        actions = []
        # Ajouter les actions possibles en fonction de l'état actuel
        return actions

    def result(self, state, action):
        # Appliquer l'action à l'état actuel et retourner le nouvel état
        new_state = state.copy()
        # Mettre à jour new_state en fonction de l'action
        return new_state

    def goal_test(self, state):
        # Vérifier si l'état actuel est l'état cible
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        # Retourner le coût du chemin
        return c + 1

    def h(self, node):
        # Heuristique pour l'algorithme A*
        return 0  # Par défaut, utiliser une heuristique nulle

def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip().split() for line in file]

def main(init_file, goal_file):
    initial = read_file(init_file)
    goal = read_file(goal_file)
    problem = PuzzleProblem(initial, goal)

    # Choisir une stratégie de recherche
    solution = breadth_first_tree_search(problem)

    # Afficher la solution
    for state in solution.path():
        for row in state.state:
            print(' '.join(row))
        print()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python puzzle.py <init_file> <goal_file>")
    else:
        init_file = sys.argv[1]
        goal_file = sys.argv[2]
        main(init_file, goal_file)
