 # puzzle.py

from aima.search import Problem, breadth_first_tree_search
import sys

class PuzzleProblem(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        # Définir les actions possibles (mouvements glissants)
        actions = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == '0':
                    if i > 0: actions.append(('up', (i, j)))
                    if i < len(state) - 1: actions.append(('down', (i, j)))
                    if j > 0: actions.append(('left', (i, j)))
                    if j < len(state[i]) - 1: actions.append(('right', (i, j)))
        return actions

    def result(self, state, action):
        # Appliquer l'action à l'état actuel et retourner le nouvel état
        new_state = [row[:] for row in state]
        direction, (i, j) = action
        if direction == 'up':
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        elif direction == 'down':
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        elif direction == 'left':
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        elif direction == 'right':
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        return new_state

    def goal_test(self, state):
        # Vérifier si l'état actuel est l'état cible
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        # Retourner le coût du chemin
        return c + 1

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
    if solution:
        for state in solution.path():
            for row in state.state:
                print(' '.join(row))
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python puzzle.py <init_file> <goal_file>")
    else:
        init_file = sys.argv[1]
        goal_file = sys.argv[2]
        main(init_file, goal_file)
