""" Runner code to exercise the Life/GraphicLife classes """

from reversi import *
from text_player import *
from random_player import *
from minimax_player import *
from text_ui import *

def run():
    ui = GraphicUI()
    player1 = MinimaxPlayer(1, 3)
    player2 = TextPlayer(2)    
    players = []
    players.append(player1)
    players.append(player2)

    player1_score = 0
    player2_score = 0
    tie = 0
    i = 0
    while i < 1:
        result = reversi(players, ui)
        if result == 1:
            player1_score = player1_score + 1
            i += 1
        elif result == 2:
            player2_score = player2_score + 1
            i += 1
        else:
            tie = tie + 1
            i += 1
    print("*" * 15)
    print("Player 1 Score = {}".format(player1_score))
    print("Player 2 Score = {}".format(player2_score))
    print("Tie = {}".format(tie))

run()

