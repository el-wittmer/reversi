from player import Player
from board import Board
import random

class MinimaxPlayer(Player):
    def __init__(self, pnum, depth):
        """
        Initialize Player class for a given player num (either 1 or 2).
        """
        self.pnum = pnum
        self.depth = depth
        self.corners = [(0,0),(0,7),(7,0),(7,7)]
        self.edges = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),\
                      (1,0),(1,7),\
                      (2,0),(2,7),\
                      (3,0),(3,7),\
                      (4,0),(4,7),\
                      (5,0),(5,7),\
                      (6,0),(6,7),\
                      (7,1),(7,2),(7,3),(7,4),(7,5),(7,6)]
        self.death_zone = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),\
                   (2,1),(2,6),\
                   (3,1),(3,6),\
                   (4,1),(4,6),\
                   (5,1),(5,6),\
                   (6,1),(6,2),(6,3),(6,4),(6,5),(6,6)] # second to last outer ring
                   
        self.safe_move = {(1,1):[(1,0),(0,1)],(1,2):[(0,2)],(1,3):[(0,3)],(1,4):[(0,4)],(1,5):[(0,5)],(1,6):[(0,6),(1,7)],\
                          (2,1):[(2,0)],(2,6):[(2,7)],\
                          (3,1):[(3,0)],(3,6):[(3,7)],\
                          (4,1):[(4,0)],(4,6):[(4,7)],\
                          (5,1):[(5,0)],(5,6):[(5,7)],\
                          (6,1):[(6,0),(7,1)],(6,2):[(7,2)],(6,3):[(7,3)],(6,4):[(7,4)],(6,5):[(7,5)],(6,6):[(7,6),(6,7)] }

    def chooseMove(self, board, moves):
        best_move = self.getBestMove(self.pnum, board, moves)
        return best_move
        
    def getBestMove(self, pnum, board, moves):
        best_score = 0.0
        best_move = []
        for move in moves:
            score = 0.0
            if (move in self.corners):
                score = 2
            elif (move in self.edges):
                score = 1        
            elif (move in self.death_zone):   # see if in second to last outer
                edge_pieces = self.safe_move[move]
                for edge_piece in edge_pieces:
                    type = board.at(move)
                    if type == self.pnum:
                        score = 1.5
                    else:
                        score = 0
            else:            
                board_copy = self.boardCopy(board) # try minimax score
                board_copy.makeMove(pnum, move)          
                legal_moves = board_copy.legalMoves(board.opponent(pnum)) # ensure more legal moves
                if len(legal_moves) > 0:
                    if board_copy.moves() < 60:
                        score = self.minimax(board_copy, board.opponent(pnum), self.depth) # returns a ratio
                else:
                    if board.playerScore(board.opponent(self.pnum)) != 0:
                        score = board.playerScore(self.pnum) / (board.playerScore(board.opponent(self.pnum)) + board.playerScore(self.pnum))
                    else:
                        score = .99
                score = self.__evaporation(board, score)
            if score >= best_score:
                best_score = score
                best_move = move
        return best_move
        
    def minimax(self, board, player, depth):
        score = 0.0
        if board.moves() >= 60 or depth == 0: # if there are no legal moves or the function is done running
            ratio = 0.0
            if board.playerScore(board.opponent(self.pnum)) != 0:
                ratio = board.playerScore(self.pnum) / (board.playerScore(board.opponent(self.pnum)) + board.playerScore(self.pnum))
            else:
                ratio = .99  #
            return ratio
        else:
            if player == self.pnum: #this is the current player
                moves = board.legalMoves(self.pnum)
                if len(moves) > 0:
                    for move in moves: #for all the legal moves this player can make:
                        b = Board()
                        b = self.boardCopy(board) #create a temporary board that saves this move
                        b.makeMove(self.pnum, move) #modify the board based on this move
                        branch_score = 0.0
                        branch_score = self.minimax(b, board.opponent(self.pnum), depth-1)
                        score = (float(branch_score) + score) / 2
                         #call this function again with the other player
                return score #after cycling through all the possible moves
            else:
                moves = board.legalMoves(board.opponent(self.pnum)) #for all the legal moves of the opponent (using the temp board)
                if len(moves) > 0:
                    for move in moves:
                        b = Board()
                        b = self.boardCopy(board) #create a temporary board that saves this move
                        b.makeMove(board.opponent(self.pnum), move) #modify the board based on this move
                        #modify board b based on m 
                        branch_score = 0.0
                        branch_score = self.minimax(b, self.pnum, depth-1)                   
                        score = (float(branch_score) + score) / 2 #call this function with the original player
                return score
        
    def boardCopy(self, board):
        board_copy = Board()
        i = 0
        while i < 8:
            row = []
            j = 0
            while j < 8:
                yx = []
                yx.append(i)
                yx.append(j)
                row.append(board.at(yx))
                j = j + 1
            board_copy.board[i] = row
            i = i + 1
        return board_copy

    def __evaporation(self, board, score):
        result = 0.0
        if board.moves() < 54:
            if score > 0 and score < 1:
                result = 1 - score
            else:
                result = score
        return result

            
                