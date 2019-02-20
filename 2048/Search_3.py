from Utility_3 import Utility
import time
from Helper import *

inf = float("inf")
class Search():
    def __init__(self):
        self.search_depth = 0

    def get_optimal_move(self, grid):
        return

    def to_file(self, data):
        file = open("time taken.txt", 'a')
        time_taken, moves_len, utility = data
        overpoint2 = "-------------------> here" if time_taken > 0.25 else 0
        to_write = str(time_taken) + "\t" + str(moves_len) + "\t" + str(utility) + "\t" + str(overpoint2) + "\n"
        file.write(to_write)
        file.close()