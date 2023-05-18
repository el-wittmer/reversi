"""
Project 3 - text_player.py
Elaina Wittmer
elwittmer
"""
from player import *
from board import *
from graphics import Point

class TextPlayer(Player):
    def __init__(self, pnum):
        self.pnum = pnum

    def chooseMove(self, board, moves):
        while True:
            yx = []
            s = input('Type a y,x pair (no parens): ')
            if len(s) >= 3:
                y = s[0]
                if y in ['0','1','2','3','4','5','6','7']:
                    yx.append(int(y))
                x = s[2]
                if y in ['0','1','2','3','4','5','6','7']:
                    yx.append(int(x))
            if tuple(yx) in moves:
                break   
            
        return yx

class GraphicPlayer(Player):
    def __init__(self, pnum, ui):
        """
        Initialize Player class for a given player num (either 1 or 2).
        """
        self.pnum = pnum
        self.ui = ui

    def chooseMove(self, board, moves):
        """
        Given a non-empty list of legal moves (which are (y,x) tuples),
        choose and return one of these moves to make next.
        """
        while True:
            try:
                clicked = self.ui.window.getMouse() #takes the mouse's click, converts into the coordinate system board.at() uses.
                YX = []
                YX.append((clicked.getX()-4)//75)
                YX.append((clicked.getY()-4)//75)
                if tuple(YX) in moves:
                    return YX
            except: #if the window is exited out of before a move is chosen, this tries to neaten up the errors that amount in the background. 
                print("~~~~~~~~~goodbye!~~~~~~~~~") #(unfortunately I can't pretty them all up without changing reversi.py)
                break
        