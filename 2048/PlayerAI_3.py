from Search_3 import Search
from BaseAI_3 import BaseAI
from Minimaxab import *
from Helper import *
import time


class PlayerAI(BaseAI):
    def __init__(self):
        self.search = Search()
        return

    def getMove(self, grid):
        move = self.optimal_move(grid)
        return move

    # def getMove(self, grid):
    #     moves = grid.getAvailableMoves()
    #     maxUtility = -np.inf
    #     nextDir = -1
    #
    #     for move in moves:
    #         child = getChild(grid, move)
    #
    #         utility = Decision(grid=child, max=False)
    #
    #         if utility >= maxUtility:
    #             maxUtility = utility
    #             nextDir = move
    #     print(maxUtility)
    #     return nextDir

    def optimal_move(self, grid):
        move = self.search.get_optimal_move(grid)
        return move


