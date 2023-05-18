"""
    Graphic Methods (bits copied directly from their respective classes)

    by Emmett Kahn (kahnru) and Elaina Wittmer
"""
from ui import *
from player import *
import time
from board import *
from graphics import *



class GraphicUI(UI):
    def __init__(self):
        """
        Initialize UI class
        """       
        width = 8
        height = 8
        self.prevboard = [[0 for x in range(width)] for x in range(height)] #to help with transitions, a blank board
        global window
        window = GraphWin("reversi", 75*width, 100+75*height, autoflush=False) #makes the graphics window 600x700
        window.setBackground(color_rgb(156,226,156))
        background = Image(Point(2+75*width/2, 2+75*height/2), "/Users/ruthkahn/Desktop/pr3_files/bg.gif") 
        #sets the background at the point (300,300)
        background.draw(window) #draws the background
        self.images = []
        for row in range(0,height): #initializing every possible state of graphics for any possible board state. 
            lis = []
            for collumn in range(0,width):
                col = collumn*75+39,
                ro = row*75+39
                white1 = Image(Point(col, ro), "/Users/ruthkahn/Desktop/pr3_files/white1.gif")
                white2 = Image(Point(col, ro), "/Users/ruthkahn/Desktop/pr3_files/white2.gif")
                white  = Image(Point(col, ro), "/Users/ruthkahn/Desktop/pr3_files/white.gif")
                grey1  = Image(Point(col, ro), "/Users/ruthkahn/Desktop/pr3_files/grey1.gif")
                grey2  = Image(Point(col, ro), "/Users/ruthkahn/Desktop/pr3_files/grey2.gif")
                black  = Image(Point(col, ro), "/Users/ruthkahn/Desktop/pr3_files/black.gif")
                black2 = Image(Point(col, ro), "/Users/ruthkahn/Desktop/pr3_files/black2.gif")
                black1 = Image(Point(col, ro), "/Users/ruthkahn/Desktop/pr3_files/black1.gif")
                lis.append([white1, white2, white, grey1, grey2, black, black2, black1])
            self.images.append(lis)
        #####setting the text up
        self.p1_text =    Text(Point(100,75*height+25), "Player 1: 02") #setting the text
        self.p2_text =    Text(Point(500,75*height+25), "Player 2: 02") 
        self.moves_text = Text(Point(300,75*height+25), "Moves: 00")
        #####changing the text around to something prettier
        textcolor = color_rgb(29, 129, 100)
        textsize  = 20
        self.p1_text.setTextColor(textcolor)
        self.p2_text.setTextColor(textcolor)
        self.moves_text.setTextColor(textcolor)
        self.p1_text.setFace('courier')
        self.p2_text.setFace('courier')
        self.moves_text.setFace('courier')
        self.p1_text.setSize(20)
        self.p2_text.setSize(20)
        self.moves_text.setSize(20)
        self.p1_text.draw(window)
        self.p2_text.draw(window)
        self.moves_text.draw(window)
        #####extra text: title and subtitle:
        self.title_text = Text(Point(300,75*height+52), "Reversi")
        self.title_text.setTextColor(color_rgb(54, 141, 115))
        self.title_text.setFace('courier')
        self.title_text.setSize(34)
        self.title_text.draw(window)
        subtitle_text = Text(Point(300,75*height+80), "(by Elaina Wittmer and Emmett Kahn)")
        subtitle_text.setTextColor(color_rgb(33,173,119))
        subtitle_text.setFace('courier')
        subtitle_text.setSize(15)
        subtitle_text.draw(window)
        window.update()


        

    def showBoard(self, board):
        """
        simply tranistions to the next board space using showMove. 
        Should do nothing except on the first turn, where it should 
        transition to the first boardstate.
        """  
        for row in range(0, 8): #draws the correct board at the time the board happens
            for tile in range(0,8):
                if board.at([row,tile])==1:
                    try:
                        self.images[tile][row][5].undraw()
                    except:
                        pass
                    try: 
                        self.images[tile][row][2].draw(window)
                    except: 
                        pass
                if board.at([row,tile])==2:
                    try:
                        self.images[tile][row][2].undraw()
                    except:
                        pass
                    try: 
                        self.images[tile][row][5].draw(window)
                    except: 
                        pass
        window.update()
        

    def showLegalMoves(self, moves, pnum):
        """
        Present the available legal moves at the current board state for player pnum
        basic small transition, should briefely flash the next legal move on the screen,
        then take them away again, so that the player can click on their next move. 
        """ 
        for tupl in moves:
            #############first phase############ translucent tiles
            if pnum == 1:
                self.images[tupl[1]][tupl[0]][0].draw(window)
            if pnum == 2:
                self.images[tupl[1]][tupl[0]][7].draw(window)
        window.update()
        time.sleep(.1)
            #############second phase########### less translucent tiles
        for tupl in moves:
            if pnum == 1:
                self.images[tupl[1]][tupl[0]][0].undraw()
                self.images[tupl[1]][tupl[0]][1].draw(window)
            if pnum == 2:
                self.images[tupl[1]][tupl[0]][7].undraw()
                self.images[tupl[1]][tupl[0]][6].draw(window)
        window.update()
        time.sleep(.3)
        #############third phase############ previous tiles
        for tupl in moves:
            if pnum == 1:
                self.images[tupl[1]][tupl[0]][1].undraw()
                self.images[tupl[1]][tupl[0]][0].draw(window)
            if pnum == 2:
                self.images[tupl[1]][tupl[0]][6].undraw()
                self.images[tupl[1]][tupl[0]][7].draw(window)
        window.update()
        time.sleep(.1)
        ##############fourth phase########## undrawing everything
        for tupl in moves:
            if pnum == 1:
                self.images[tupl[1]][tupl[0]][0].undraw()
            if pnum == 2:
                self.images[tupl[1]][tupl[0]][7].undraw()
        window.update()

        

    def showMove(self, board, captured, last = False):
        """
        Optional: present any special effect (if desired), when a given
        move is taken.
        Receives the board, the list of (y,x) captured pieces,
        and a boolean indicating whether this was the last move.

        Since the function captured doesn't actually specify if a 
        piece is going from white to black or from blank to black,
        my function actually has to keep track of what the previous 
        board looks like, as well, instead of using the captured variable at all.

        The ending animations will first take away pairs of black and white 
        tiles until there is none of at least one color tile. Then the rest of the tiles,
        if there are any left, will fade out of existence, and the text color of the title 
        will turn the color of the winner, or stay neutral if there is no winner. 
        """
        if last == True: 
            p1 = []
            p2 = []
            for row in range(0, 8): #setting out the order of disappearing tiles: 
                for tile in range(0,8): #black ones go from the bottom right up, white ones from the top left down. 
                    if board.at((row,tile)) == 1:
                        p1.append((tile,row))
                    if board.at((row,tile)) == 2:
                        p2.insert(0,(tile,row))
            i=0
            for i in range(0, min(len(p1), len(p2))): #dissapearing pairs of tiles at a time
                self.images[p1[i][0]][p1[i][1]][2].undraw()
                self.images[p2[i][0]][p2[i][1]][5].undraw()
                window.update()
                time.sleep(.1)
                i+=1
            time.sleep(.2)
            if board.playerScore(1) > board.playerScore(2): #changing the color of the title by increments
                self.title_text.setTextColor(color_rgb(85,159,138))
            elif board.playerScore(1) < board.playerScore(2):
                self.title_text.setTextColor(color_rgb(64,114,99))
            for tupl in p1[i:]: #fading out the leftover tiles by incriments
                self.images[tupl[0]][tupl[1]][2].undraw()
                self.images[tupl[0]][tupl[1]][1].draw(window)
            for tupl in p2[i:]:
                self.images[tupl[0]][tupl[1]][5].undraw()
                self.images[tupl[0]][tupl[1]][6].draw(window)
            window.update()
            time.sleep(.1)
            if board.playerScore(1) > board.playerScore(2):#changing the color of the title by increments
                self.title_text.setTextColor(color_rgb(128,178,163))
            elif board.playerScore(1) < board.playerScore(2):
                self.title_text.setTextColor(color_rgb(72,93,87))
            for tupl in p1[i:]:#fading out the leftover tiles by incriments
                self.images[tupl[0]][tupl[1]][1].undraw()
                self.images[tupl[0]][tupl[1]][0].draw(window)
            for tupl in p2[i:]:
                self.images[tupl[0]][tupl[1]][6].undraw()
                self.images[tupl[0]][tupl[1]][7].draw(window)
            window.update()
            time.sleep(.1)
            if board.playerScore(1) > board.playerScore(2):#changing the color of the title by increments
                self.title_text.setTextColor(color_rgb(234,234,234))
            elif board.playerScore(1) < board.playerScore(2):
                self.title_text.setTextColor(color_rgb(83,83,83))
            for tupl in p1[i:]:#fading out the leftover tiles by incriments
                self.images[tupl[0]][tupl[1]][0].undraw()
            for tupl in p2[i:]:
                self.images[tupl[0]][tupl[1]][7].undraw()
            window.update()
        ##################################################for individual moves###############################################################
        else:
            blacktowhite = []
            whitetoblack = []
            fadetoblack  = []
            fadetowhite  = []
            pre = self.prevboard
            lis = []
            bo  = []
            for row in range(0, 8): #basic tiles
                lis = []
                for tile in range(0,8):
                    lis.append(board.at([row,tile]))
                    if board.at([row,tile])==1: #making a list of spaces where white tiles will be needed
                        if   pre[row][tile]==0:
                            fadetowhite.append((row,tile))
                        elif pre[row][tile]==2:
                            blacktowhite.append((row,tile))
                    elif board.at([row,tile])==2: #making a list of spaces where black tiles will be needed
                        if   pre[row][tile]==0:
                            fadetoblack.append((row,tile))
                        elif pre[row][tile]==1:
                            whitetoblack.append((row,tile))
                bo.append(lis)
            #next up, controlling the actual animations, such that the board looks pretty all the way through ~
            ################first phase###############
            for tupl in fadetowhite:  #tiles changing
                self.images[tupl[1]][tupl[0]][0].draw(window)
            for tupl in fadetoblack:
                self.images[tupl[1]][tupl[0]][7].draw(window)
            for tupl in whitetoblack:
                self.images[tupl[1]][tupl[0]][2].undraw()
                self.images[tupl[1]][tupl[0]][3].draw(window)
            for tupl in blacktowhite:
                self.images[tupl[1]][tupl[0]][5].undraw()
                self.images[tupl[1]][tupl[0]][4].draw(window)
            self.p1_text.undraw() #text transition
            self.p2_text.undraw()
            self.moves_text.undraw()
            self.p1_text.setText("Player 1: " + "a?")
            self.p2_text.setText("Player 2: " + "?b")
            self.moves_text.setText("Moves: " + "##")
            self.p1_text.draw(window) #redraws the text
            self.p2_text.draw(window)
            self.moves_text.draw(window)
            window.update()
            time.sleep(.1)
            ################second phase################
            for tupl in fadetowhite:
                self.images[tupl[1]][tupl[0]][0].undraw()
                self.images[tupl[1]][tupl[0]][1].draw(window)
            for tupl in fadetoblack:
                self.images[tupl[1]][tupl[0]][7].undraw()
                self.images[tupl[1]][tupl[0]][6].draw(window)
            for tupl in whitetoblack:
                self.images[tupl[1]][tupl[0]][3].undraw()
                self.images[tupl[1]][tupl[0]][4].draw(window)
            for tupl in blacktowhite:
                self.images[tupl[1]][tupl[0]][4].undraw()
                self.images[tupl[1]][tupl[0]][3].draw(window)
            self.p1_text.undraw() #text transition
            self.p2_text.undraw()
            self.moves_text.undraw()
            self.p1_text.setText("Player 1: " + "##")
            self.p2_text.setText("Player 2: " + "a?")
            self.moves_text.setText("Moves: " + "?b")
            self.p1_text.draw(window) #redraws the text
            self.p2_text.draw(window)
            self.moves_text.draw(window)
            window.update()
            time.sleep(.1)
            window.update()
            #####################text########################
            self.p1_text.undraw()#undraws the text before changing it
            self.p2_text.undraw()
            self.moves_text.undraw()
            if (board.playerScore(1))//10==0:
                self.p1_text.setText("Player 1: 0" + str(board.playerScore(1)))
            else:
                self.p1_text.setText("Player 1: " + str(board.playerScore(1)))
            if (board.playerScore(2))//10==0:
                self.p2_text.setText("Player 2: 0" + str(board.playerScore(2)))
            else:
                self.p2_text.setText("Player 2: " + str(board.playerScore(2)))
            if (board.moves())//10==0:
                self.moves_text.setText("Moves: 0" + str(board.moves()))
            else:
                self.moves_text.setText("Moves: " + str(board.moves()))
            self.p1_text.draw(window) #redraws the text
            self.p2_text.draw(window)
            self.moves_text.draw(window)
            window.update()
            #################################################
            self.prevboard = []
            for lis in bo:
                self.prevboard.append(list(lis))
            #################third phase####################
            for tupl in fadetowhite:
                self.images[tupl[1]][tupl[0]][1].undraw()
                #self.images[tupl[1]][tupl[0]][2].draw(window)
            for tupl in fadetoblack:
                self.images[tupl[1]][tupl[0]][6].undraw()
                #self.images[tupl[1]][tupl[0]][5].draw(window)
            for tupl in whitetoblack:
                self.images[tupl[1]][tupl[0]][4].undraw()
                #self.images[tupl[1]][tupl[0]][5].draw(window)
            for tupl in blacktowhite:
                self.images[tupl[1]][tupl[0]][3].undraw()
                #self.images[tupl[1]][tupl[0]][2].draw(window)
            time.sleep(.1)






class GraphicPlayer(Player):
    def __init__(self, pnum):
        """
        Initialize Player class for a given player num (either 1 or 2).
        """
        self.pnum = pnum

    def chooseMove(self, board, moves):
        """
        Given a non-empty list of legal moves (which are (y,x) tuples),
        choose and return one of these moves to make next.
        """
        while True:
            try:
                clicked = window.getMouse() #takes the mouse's click, converts into the coordinate system board.at() uses. 
                X = (clicked.getX()-4)//75
                Y = (clicked.getY()-4)//75
                if (X,Y) in moves:
                    return (X,Y)
            except: #if the window is exited out of before a move is chosen, this tries to neaten up the errors that amount in the background. 
                print("~~~~~~~~~goodbye!~~~~~~~~~") #(unfortunately I can't pretty them all up without changing reversi.py)
                break

