from Search_3 import Search
from BaseAI_3 import BaseAI
import time


class PlayerAI(BaseAI):
    def __init__(self):
        return

    def getMove(self, grid):
        move = self.optimal_move(grid)
        return move

    def optimal_move(self, grid):
        move = Search().get_optimal_move(grid)
        return move


