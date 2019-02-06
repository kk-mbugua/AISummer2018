from Grid_3 import Grid
import math
import time


class Utility:
    def __init__(self):
        return

    def get_utility(self, grid):
        es = self.empty_squares(grid)
        ev = self.edge_values(grid)
        nd = self.neighbour_diff(grid)
        ss = self.s_shape(grid)
        mt = self.max_value(grid)

        utility = nd*-0.5 + ev*2 + es*7 + ss*10 + mt*2
        #print("search utility", utility)
        return utility

    def empty_squares(self, grid):
        """Returns the number of empty squares. The more empty squares the more advantageous"""
        return len(grid.getAvailableCells())

    def edge_values(self, grid):
        """Returns a weighted sum of the values on the edge of the grid. The higher the sum
        the more advantageous"""
        sum = 0
        for x in range(grid.size):
            for y in range(grid.size):
                if x == 0 or y == 0:
                    cell_value = grid.getCellValue((x,y))
                    if cell_value != 0:
                        sum += math.log(grid.getCellValue((x, y)), 2)

        return sum

    def get_neighbours(self, pos):
        preliminary_neighbours = []
        neighbours = []
        x = pos[0]
        y = pos[1]
        up = (x-1, y)
        right = (x, y+1)
        down = (x+1, y)
        left = (x, y-1)
        preliminary_neighbours.append(up)
        preliminary_neighbours.append(right)
        preliminary_neighbours.append(down)
        preliminary_neighbours.append(left)

        for pn in preliminary_neighbours:
            if pn[0] > -1 and pn[1] > -1:
                neighbours.append(pn)

        return neighbours

    def neighbour_diff(self, grid):
        sum_of_differences = 0
        for x in range(grid.size):
            for y in range(grid.size):
                pos = (x, y)
                pos_value = grid.getCellValue(pos)
                pos_log_value = math.log(grid.getCellValue(pos), 2) if (pos_value != None and pos_value != 0) else 0
                neighbours = self.get_neighbours(pos)
                for n in neighbours:
                    n_value = grid.getCellValue(n)
                    n_log_value = math.log(n_value) if (n_value != None and n_value != 0) else 0
                    diff = abs(n_log_value-pos_log_value)
                    sum_of_differences += diff

        return sum_of_differences

    def s_shape(self, grid):
        size = grid.size
        weight = size ** 2 -1
        value = 0
        for x in range(size):
            for y in range(size):
                value += grid.getCellValue((x, y)) * weight
        return math.log(value, 2)

    def max_value(self, grid):
        return math.log(grid.getMaxTile(), 2)

    def possible_merges(self, grid):
        merges = 0
        for x in range(grid.size):
            for y in range(grid.size):
                pos = (x, y)
                pos_value = grid.getCellValue()
                neighbours = self.get_neighbours(pos)
                for n in neighbours:
                    if pos_value == grid.getCellValue(n):
                        merges += 1
        return merges

if __name__ == "__main__":
    grid = Grid()
    a = grid.getAvailableCells()
    print(len(a))
