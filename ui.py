"""
    Template Base class for a Reversi user interface class.
    This class contains the (unimplemented) minimimum
    required interface to interface with a human player. You should inherit 
    your UI classes from this class and override these methods.
    You should *not* be modifying this class or file.
    You may also add private methods and data attributes to your
    derived classes as you see fit, but you may NOT change the
    interface (parameters) of any method
"""

class UI:
    def __init__(self):
        """
        Initialize UI class
        """
        pass

    def showBoard(self, board):
    	"""
    	Present the entire board state, player scores, and no. of moves
    	"""
    	pass

    def showLegalMoves(self, moves, pnum):
    	"""
    	Present the available legal moves at the current board state for player pnum
    	"""
    	pass

    def showMove(self, board, captured, last = False):
    	"""
    	Optional: present any special effect (if desired), when a given
    	move is taken.
    	Receives the board, the list of (y,x) captured pieces,
    	and a boolean indicating whether this was the last move.
    	"""
    	pass
