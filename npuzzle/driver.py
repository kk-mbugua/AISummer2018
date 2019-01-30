import time
import resource
import queue
import sys
import math

#### SKELETON CODE ####

## The Class that Represents the Puzzle
class PuzzleState(object):
    """docstring for PuzzleState"""
    def __init__(self, config, n, parent=None, action="Initial", cost=0, actions= []):
        if n*n != len(config) or n < 2:
            raise Exception("the length of config is not correct!")
        self.n = n
        self.cost = cost
        self.parent = parent
        self.action = action
        self.dimension = n
        self.config = config
        self.children = []
        self.actions.append(action)
        for i, item in enumerate(self.config):
            if item == 0:
                self.blank_row = int(i / self.n)
                self.blank_col = int(i % self.n)
                break

    def display(self):
        for i in range(self.n):
            line = []
            offset = i * self.n
            for j in range(self.n):
                line.append(self.config[offset + j])
            print(line)

    def move_left(self):
        if self.blank_col == 0:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index - 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):
        if self.blank_col == self.n - 1:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index + 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):
        if self.blank_row == 0:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index - self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):
        if self.blank_row == self.n - 1:
            return None
        else:
            blank_index = self.blank_row * self.n + self.blank_col
            target = blank_index + self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):
        """expand the node"""
        # add child nodes in order of UDLR
        if len(self.children) == 0:
            up_child = self.move_up()
            if up_child is not None:
                self.children.append(up_child)
            down_child = self.move_down()
            if down_child is not None:
                self.children.append(down_child)
            left_child = self.move_left()
            if left_child is not None:
                self.children.append(left_child)
            right_child = self.move_right()
            if right_child is not None:
                self.children.append(right_child)
        return self.children


# Function that Writes to output.txt
### Students need to change the method to have the corresponding parameters
def writeOutput():
    file = open("output.txt", 'w')

    return


def bfs_search(initial_state):
    """BFS search"""
    frontier = queue.Queue()
    expanded = []
    frontier.put(initial_state)
    while not frontier.empty():
        state = frontier.get()
        if state.config in expanded:
            continue
        if test_goal(state):
            print("Yaaaaay, found")
            return True
        children = state.expand()
        expanded.append(state.config)
        for element in children:
            frontier.put(element)
    print("Sorry Fam!")
    return False


def dfs_search(initial_state):
    """DFS search"""
    frontier = queue.LifoQueue()
    expanded = []
    frontier.put(initial_state)

    while not frontier.empty():
        state = frontier.get()
        if state.config in expanded:
            continue
        if test_goal(state):
            print("Yaaaaay, found")
            return True
        children = state.expand()
        expanded.append(state.config)
        for element in reversed(children):
            frontier.put(element)

    print("Sorry Fam!")
    return False


def A_star_search(initial_state):
    """A * search"""
    frontier = {}
    expanded = []
    frontier[initial_state] = initial_state.cost

    while frontier:
        state = lowest_state(frontier)
        del frontier[state]
        if state.config in expanded:
            continue
        if test_goal(state):
            print("Yaaaaay, found")
            return True
        children = state.expand()
        expanded.append(state.config)
        for element in children:
            frontier[element] = element.cost + total_manhattan(element)

    print("Sorry Fam!")
    return False


def lowest_state(frontier):
    lowest_value = 100000000000
    lowest_key = tuple()
    for key, value in frontier.items():
        if value < lowest_value:
            lowest_key = key
    return lowest_key


def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""
    diff = abs(idx-value)
    count = 0
    while diff >= n:
        diff -= n
        count += 1
    return count+diff


def total_manhattan(state):
    manhattan = 0
    for index, num in enumerate(state.config):
        manhattan += calculate_manhattan_dist(index, num, state.n)
    return manhattan


def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    goal = []
    for i in range(puzzle_state.n**2):
        goal.append(i)

    if tuple(goal) == puzzle_state.config:
        return True
    else:
        return False


# Main Function that reads in Input and Runs corresponding Algorithm
def main():
    sm = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = tuple(map(int, begin_state))
    size = int(math.sqrt(len(begin_state)))
    hard_state = PuzzleState(begin_state, size)

    if sm == "bfs":
        bfs_search(hard_state)
    elif sm == "dfs":
        dfs_search(hard_state)
    elif sm == "ast":
        A_star_search(hard_state)
    else:
        print("Enter valid command arguments !")


if __name__ == '__main__':
    main()

