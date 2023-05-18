from ui import UI
from board import Board

"""
    Main game file for Reversi
    The main game loop receives two strategies (Player class) in a list,
    and a UI class to present the board and moves (default: no presentation)
    It then alternates making moves until no more moves are available.
    It returns the number of the player who won (or zero for a tie)
"""

def reversi(players, ui = UI()):
    board = Board()
    pnum = 1
    skipped = 0

    while skipped < 2:
        ui.showBoard(board)
        moves = board.legalMoves(pnum)
        ui.showLegalMoves(moves, pnum)
        if len(moves) > 0:
            move = players[pnum - 1].chooseMove(board, moves)
            captured = board.makeMove(pnum, move)
            ui.showMove(board, captured)
            skipped = 0
        else:
            skipped += 1
        pnum = board.opponent(pnum)

    ui.showMove(board, captured, True)
    if board.playerScore(1) > board.playerScore(2):
        return 1
    elif board.playerScore(2) > board.playerScore(1):
        return 2
    else:
        return 0
