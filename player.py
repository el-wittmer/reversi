"""
    Template Base class for a Reversi game Player class
    This class contains the (unimplemented) minimimum
    required interface for a player (strategy). You should inherit 
    your Player classes from this class and override these methods.
    You should *not* be modifying this class or file.
    You may also add private methods and data attributes to your
    derived classes as you see fit, but you may NOT change the
    interface (parameters) of chooseMove().
"""

class Player:
    def __init__(self, pnum):
        """
        Initialize Player class for a given player num (either 1 or 2).
        """
        pass

    def chooseMove(self, board, moves):
        """
        Given a non-empty list of legal moves (which are (y,x) tuples),
        choose and return one of these moves to make next.
        """
        pass
