from Utility_3 import Utility
import time

inf = float("inf")
class Search():
    def __init__(self):
        self.should_time = True
        self.max_search_depth = 12
        self.alpha = -inf
        self.beta = inf
        self.max_book = []
        self.min_book = []

    def get_optimal_move(self, grid):

        time_before = time.clock()
        optimal_move, utility = self.maximize(grid)

        print("optimal", optimal_move)
        print("utility", utility)
        time_after = time.clock()
        data = (time_after - time_before), len(grid.getAvailableMoves()), utility
        self.to_file(data) if self.should_time else None
        print("\toptimal move =", optimal_move)
        return optimal_move

    def maximize(self, grid):
        if self.is_terminal_node(grid):
            return None, self.utility_calculator(grid)

        best_move, max_utility = None, -inf

        for m in grid.getAvailableMoves():
            new_grid = grid.clone()
            new_grid.move(m)

            _, utility = self.minimize(new_grid)

            if utility > max_utility:
                best_move = m
                max_utility = utility

            self.alpha = max(utility, self.alpha)
            if self.beta <= self.alpha:
                break

        return best_move, max_utility

    def minimize(self, grid):
        worst_placement, min_utility = None, inf

        available_tiles = grid.getAvailableCells()

        for tile in available_tiles:
            utility = self.chance(grid, tile)

            if utility < min_utility:
                min_utility = utility
                worst_placement = tile

            self.beta = min(utility, self.beta)
            if self.beta <= self.alpha:
                break

        return worst_placement, min_utility

    def chance(self, grid, tile):
        values = [(2, 0.9), (4, 0.1)]
        avg_utility = 0
        for value in values:
            new_grid = grid.clone()
            new_grid.insertTile(tile, value[0])
            _, utility = self.maximize(new_grid)
            avg_utility += utility * value[1]

        return avg_utility

    def utility_calculator(self, grid):
        return Utility().get_utility(grid)

    def is_terminal_node(self, grid):
        if self.max_search_depth <= 0 or len(grid.getAvailableMoves()) <= 0:
            return True
        else:
            self.inc_search_depth()
        return False

    def get_children(self, grid, moves):
        children = []
        for move in moves:
            child_grid = grid.clone().move(move)
            children.append(child_grid)
        return children

    def inc_search_depth(self):
        self.max_search_depth -= 1
        return

    def to_file(self, data):
        file = open("time taken.txt", 'a')
        time_taken, moves_len, utility = data
        overpoint2 = "-------------------> here" if time_taken > 0.25 else 0
        to_write = str(time_taken) + "\t" + str(moves_len) + "\t" + str(utility) + "\t" + str(overpoint2) + "\n"
        file.write(to_write)
        file.close()