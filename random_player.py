from player import Player
import random

class RandomPlayer(Player):
    def __init__(self, pnum):
        """
        Initialize Player class for a given player num (either 1 or 2).
        """
        self._pnum = pnum

    def chooseMove(self, board, moves):
        """
        Given a non-empty list of legal moves (which are (y,x) tuples),
        choose and return one of these moves to make next.
        """
        assert(len(moves) > 0)
        return moves[random.randint(0, len(moves) - 1)]
