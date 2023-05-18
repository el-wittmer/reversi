"""
    Template inteface for a Reversi game Board class
    This class contains the (unimplemented) minimimum
    required interface for the class. You should fill in all
    the methods where it currently says "pass".
    You may also add private methods and data attributes as you
    see fit, but you may NOT change the interface of these
    public methods.
"""

class Board:
    def __init__(self):
        """
        Initialize the board to the starting state of Reversi,
        with two white discs (player 1) in locations (3,3) & (4,4)
        and two black discs in locations (4,3), (3,4)
        """
        rowzero =  [0,0,0,0,0,0,0,0]
        rowone =   [0,0,0,0,0,0,0,0]
        rowtwo =   [0,0,0,0,0,0,0,0]
        rowthree = [0,0,0,1,2,0,0,0]
        rowfour =  [0,0,0,2,1,0,0,0]
        rowfive =  [0,0,0,0,0,0,0,0]
        rowsix =   [0,0,0,0,0,0,0,0]
        rowseven = [0,0,0,0,0,0,0,0]
        self.board = [rowzero, rowone, rowtwo, rowthree, rowfour, rowfive, rowsix, rowseven]
        self.directions = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
        self.count = 0

    def at(self, loc):
        """
        Receive a location as a (y,x) tuple or [y,x] list,
        and return one of three possible values:
            0 - if there is no disc in this location
            1 - if player 1 has a disc there (white)
            2 - if player 2 has a disc there (black)
        x and y are integeres between 0 and 7.
        """
        if loc[0] < 8 and loc[0] >= 0 and loc[1] < 8 and loc[1] >= 0:
            row = self.board[loc[0]]
            cell = row[loc[1]]
            return cell
        else:
            return -1

    def playerScore(self, pnum):
        """
        For a given player number (either 1 or 2), return the
        amount of discs of the player's color on board.
        """
        player_total = 0
        for row in self.board:
            for cell in row:
                if cell == pnum:
                    player_total += 1
        return player_total        

    def moves(self):
        """
        Return the total no. of moves played so far.
        """
        return self.count


    def legalMoves(self, pnum):
        """
        for a given player number (either 1 or 2), return a
        list of (y,x) tuples where this player is allowed
        to put a new disc, based on Reversi rules. The
        list may empty if no legal moves are available.
        """
        result = []
        i = 0
        while (i < 8):
            row = self.board[i]
            j = 0
            while (j < 8):
                loc = []
                k = 0
                if row[j] == pnum:
                    loc.append(i)   # save the y
                    loc.append(j)   # save the x  
                    for direction in self.directions:
                        move = (self.__check(pnum, loc, direction))
                        if move != None:
                            if move not in result:
                                result.append(move)
                j += 1
            i += 1
        return result

    def makeMove(self, pnum, move):
        """
        Change the board state to reflect a new move by
        player pnum. The move is given as a (y,x) coordinate.
        Returns a list of (y,x) tuples (just like legalMoves()),
        of all the pieces that were captured by this move.
        """
        result=[]
        self.count += 1
        result.append(move)
        for direction in self.directions:
            cells = self.__capture(pnum, move, direction)
            if cells != None:
                for cell in cells:
                    result.append(cell)
        for item in result:
            self.__flip(pnum, item)
        return result

    def opponent(self, pnum):
        """
        For a given player number (1 or 2), return the opponent's
        player number (1 returns 2, 2 returns 1).
        """
        if pnum == 1:
            return 2
        if pnum == 2:
            return 1

    def __check(self, pnum, new_loc, direction, count=0):
        new_loc = (new_loc[0] + direction[0], new_loc[1] + direction[1]) 
        if ((new_loc[0] >= 0 and new_loc[0] < 8) and (new_loc[1] >= 0 and new_loc[1] < 8)):
            """
            Checks around the cell to see if there are any legal moves
            """
            search = self.at(new_loc)
            if search == 0 and count >= 1 or search == 7 and count >= 1:
                return new_loc
            elif search == self.opponent(pnum):               
                return self.__check(pnum, new_loc, direction, count+1)
                
    def __capture(self, pnum, move, direction, search=[], result=[], count = 0):
        if move != None:
            move = (move[0] + direction[0], move[1] + direction[1]) 
            if ((move[0] >= 0 and move[0] < 8) and (move[1] >= 0 and move[1] < 8)):
                """
                Makes sure the checked cell is not on the left or the top borders
                """
                token = self.at(move)
                if token == pnum:
                    for item in search:
                        result.append(item)
                    return result
                elif token == 0:
                    return
                elif token == self.opponent(pnum):
                    if count == 0:
                        search = []
                        result = []
                    search.append(move)            
                    return self.__capture(pnum, move, direction, search, result, count+1)
    def __flip(self, pnum, move):
        if move != None:
            row = self.board[move[0]]
            row[move[1]] = pnum
            self.board[move[0]] = row

