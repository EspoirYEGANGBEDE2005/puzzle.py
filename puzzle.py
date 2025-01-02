# Cellule 1: Imports et Définitions de Fonctions

from aima.search import Problem, breadth_first_tree_search, depth_first_tree_search, uniform_cost_search, astar_search
import time

class PuzzleProblem(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)
        self.initial = initial
        self.goal = goal

    def actions(self, state):
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
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip().split() for line in file]

def run_experiment(init_file, goal_file, search_function):
    initial = read_file(init_file)
    goal = read_file(goal_file)
    problem = PuzzleProblem(initial, goal)

    start_time = time.time()
    solution = search_function(problem)
    end_time = time.time()

    if solution:
        path = solution.path()
        steps = len(path) - 1
        nodes_explored = solution.path_cost
        return {
            "time": end_time - start_time,
            "nodes_explored": nodes_explored,
            "steps": steps,
            "path": path
        }
    else:
        return {
            "time": end_time - start_time,
            "nodes_explored": "N/A",
            "steps": "N/A",
            "path": []
        }

# Cellule 2: Définir les Fichiers d'Initialisation et de But

init_files = ["init1.txt", "init2.txt", "init3.txt", "init4.txt", "init5.txt",
              "init6.txt", "init7.txt", "init8.txt", "init9.txt", "init10.txt"]
goal_files = ["goal1.txt", "goal2.txt", "goal3.txt", "goal4.txt", "goal5.txt",
              "goal6.txt", "goal7.txt", "goal8.txt", "goal9.txt", "goal10.txt"]

# Cellule 3: Exécuter les Expérimentations

search_functions = [breadth_first_tree_search, depth_first_tree_search, uniform_cost_search, astar_search]
results = {}

for search_function in search_functions:
    search_name = search_function.__name__
    results[search_name] = []
    for init_file, goal_file in zip(init_files, goal_files):
        result = run_experiment(init_file, goal_file, search_function)
        results[search_name].append(result)

# Cellule 4: Afficher les Résultats

for search_name, search_results in results.items():
    print(f"Résultats pour {search_name}:")
    for i, result in enumerate(search_results):
        print(f"Instance {i+1}: Temps = {result['time']}, Nœuds explorés = {result['nodes_explored']}, Étapes = {result['steps']}")
        if result['path']:
            for state in result['path']:
                for row in state.state:
                    print(' '.join(row))
                print()
        else:
            print("No solution found.")
        print()
