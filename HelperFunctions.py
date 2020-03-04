'''
color coding:
1: black 
2:white 
0:unassigned
Functions:
1. update_board(board, color,pos)
        This funtion updates board after placing that specified color on that position(pos)
        pos==point object
        it returns nothing and the board passed as an argument is updated.
2. successor_func(board, color)
        This function generates all possible positions for that color in the current board
        it returns list of point objects containing possible moves fot that colors
'''

from graphics import *

# pointer class
class point:
    def __init__(self, rows, cols):
        self.row = rows
        self.col = cols

# wrapper function that will never be used directly
def upd_colors(board,color,side,ii,jj):
    # up
    if side=="up":
        if board[ii][jj]==color:
            return True
        else:
          if ii-1 >= 0:
              if upd_colors(board,color,side,ii-1,jj):
                 board[ii][jj]=color
                 return True
          return False
    # down
    if side=="down":
        if board[ii][jj]==color:
            return True
        else:
          if ii+1 < 8:
              if upd_colors(board,color,side,ii+1,jj):
                 board[ii][jj]=color
                 return True
          return False
    # right
    if side=="right":
        if board[ii][jj]==color:
            return True
        else:
          if jj+1 < 8:
              if upd_colors(board,color,side,ii,jj+1):
                 board[ii][jj]=color
                 return True
          return False              
    # left
    if side=="left":
        if board[ii][jj]==color:
            return True
        else:
          if jj-1 >= 0:
              if upd_colors(board,color,side,ii,jj-1):
                 board[ii][jj]=color
                 return True
          return False 
    # up-right
    if side=="up-right":
        if board[ii][jj]==color:
            return True
        else:
          if ii-1 >= 0 and jj+1 < 8:
              if upd_colors(board,color,side,ii-1,jj+1):
                 board[ii][jj]=color
                 return True
          return False 
    # up-left
    if side=="up-left":
        if board[ii][jj]==color:
            return True
        else:
          if ii-1 >= 0 and jj-1 >= 0:
              if upd_colors(board,color,side,ii-1,jj-1):
                 board[ii][jj]=color
                 return True
          return False
    # down-right
    if side=="down-right":
        if board[ii][jj]==color:
            return True
        else:
          if ii+1 < 8 and jj+1 < 8:
              if upd_colors(board,color,side,ii+1,jj+1):
                 board[ii][jj]=color
                 return True
          return False
    # down-left
    if side=="down-left":
        if board[ii][jj]==color:
            return True
        else:
          if ii+1 < 8 and jj-1 >= 0:
              if upd_colors(board,color,side,ii+1,jj-1):
                 board[ii][jj]=color
                 return True
          return False

# function to update board with specified color and position
# it takes point object to place that color on board
# will update all possible positions
def update_board(board, color,pos):
    board[pos.row][pos.col]=color
    if color==1:
        ncolor = 2
    else:
        ncolor = 1
    # up check
    if pos.row-1 >= 0:
        if board[pos.row-1][pos.col]==ncolor :
            upd_colors(board,color,"up",pos.row-1,pos.col)
    # down check
    if pos.row+1 < 8:
        if board[pos.row+1][pos.col]==ncolor :
            upd_colors(board,color,"down",pos.row+1,pos.col)
    # right check
    if pos.col+1 < 8:
        if board[pos.row][pos.col+1]==ncolor :
            upd_colors(board,color,"right",pos.row,pos.col+1)             
    # left check
    if pos.col-1 >= 0:
        if board[pos.row][pos.col-1]==ncolor:
            upd_colors(board,color,"left",pos.row,pos.col-1)         
    # up-right check
    if pos.row-1 >= 0 and pos.col+1 < 8:
        if board[pos.row-1][pos.col+1]==ncolor :
            upd_colors(board,color,"up-right",pos.row-1,pos.col+1) 
    # up-left check
    if pos.row-1 >= 0 and pos.col-1 >= 0:
        if board[pos.row-1][pos.col-1]==ncolor:
            upd_colors(board,color,"up-left",pos.row-1,pos.col-1)     
    # down-right check
    if pos.row+1 < 8 and pos.col+1 < 8:
        if board[pos.row+1][pos.col+1]==ncolor :
            upd_colors(board,color,"down-right",pos.row+1,pos.col+1)
    # down-left check
    if pos.row+1 < 8 and pos.col-1 >= 0:
        if board[pos.row+1][pos.col-1]==ncolor:
            upd_colors(board,color,"down-left",pos.row+1,pos.col-1)


# wrapper function that will be never used directly
# to check very next position in that direction
def avail_post(board,color,side,ii,jj):
    # up
    if side=="up":
        for i in reversed(range(ii)):
            if board[i][jj]==color:
                return None
            elif board[i][jj]==0:
                return point(i,jj)
        return None
    # down
    if side=="down":
        for i in range(ii,8):
            if board[i][jj]==color:
                return None
            elif board[i][jj]==0:
                return point(i,jj)
        return None
    # right
    if side=="right":
        for j in range(jj,8):
            if board[ii][j]==color:
                return None
            elif board[ii][j]==0:
                return point(ii,j)
        return None
    # left
    if side=="left":
        for j in reversed(range(jj)):
            if board[ii][j]==color:
                return None
            elif board[ii][j]==0:
                return point(ii,j)
        return None
    # up-right
    if side=="up-right":
        for i,j in zip(reversed(range(ii+1)), range(jj,8)):
            if board[i][j]==color:
                return None
            elif board[i][j]==0:
                return point(i,j)
        return None
    # up-left
    if side=="up-left":
        for i,j in zip(reversed(range(ii+1)), reversed(range(jj+1))):
            if board[i][j]==color:
                return None
            elif board[i][j]==0:
                return point(i,j)
        return None
    # down-right
    if side=="down-right":
        for i,j in zip(range(ii,8), range(jj,8)):
            if board[i][j]==color:
                return None
            elif board[i][j]==0:
                return point(i,j)
        return None
    # down-left
    if side=="down-left":
        for i,j in zip(range(ii,8), reversed(range(jj+1))):
            if board[i][j]==color:
                return None
            elif board[i][j]==0:
                return point(i,j)
        return None

# to check 'not in' list   
def NotIn(lst,ele): 
    for item in lst: 
        if item.row==ele.row and item.col==ele.col : 
             return False
    
    return True

# it takes board and player who's turn    color 1: black 2:white 0:unassigned
# return all possible next positions for that player.
def successor_func(board, color):
    retArr = []
    if color==1:
        ncolor = 2
    else:
        ncolor = 1
    for i in range(8):
        for j in range(8):
            if board[i][j] == color:
                # check up
                if i >= 0:
                    if board[i-1][j] == ncolor:
                        temp = avail_post(board,color,"up",i-1,j)
                        if temp is not None and NotIn(retArr,temp):
                            retArr.append(temp)
                # check down
                if i < 8:
                    if board[i+1][j] == ncolor:
                        temp = avail_post(board,color,"down",i+1,j)
                        if temp is not None and NotIn(retArr,temp):
                            retArr.append(temp)
                # check right
                if i < 8:
                    if board[i][j+1] == ncolor:
                        temp = avail_post(board,color,"right",i,j+1)
                        if temp is not None and NotIn(retArr,temp):
                            retArr.append(temp)
                # check left
                if  i >= 0:
                    if board[i][j-1] == ncolor:
                        temp = avail_post(board,color,"left",i,j-1)
                        if temp is not None and NotIn(retArr,temp):
                            retArr.append(temp)
                # check up-right
                if i >= 0 and j < 8:
                    if board[i-1][j+1] == ncolor :
                        temp = avail_post(board,color,"up-right",i-1,j+1)
                        if temp is not None and NotIn(retArr,temp):
                            retArr.append(temp)
                # check up-left
                if i >= 0 and j >= 0:
                    if board[i-1][j-1] == ncolor:
                        temp = avail_post(board,color,"up-left",i-1,j-1)
                        if temp is not None and NotIn(retArr,temp):
                            retArr.append(temp)
                # check down-right
                if i < 8 and j < 8:
                    if board[i+1][j+1] == ncolor:
                        temp = avail_post(board,color,"down-right",i+1,j+1)
                        if temp is not None and NotIn(retArr,temp):
                            retArr.append(temp)
                # check down-left
                if i < 8 and j >= 0:
                    if board[i+1][j-1] == ncolor:
                        temp = avail_post(board,color,"down-left",i+1,j-1)
                        if temp is not None and NotIn(retArr,temp):
                            retArr.append(temp)
                    
    return retArr
# evaluation function e(p)
def evaluation(board):
    white = 0
    black = 0
    for i in range(8):
        for j in range(8):
            if board[i][j]==2:
                white+=1
            elif board[i][j]==1:
                black+=1
    return white-black


# level 1 means max level
# level 0 means min level
def minmax(depth, maxdepth, level, board, nextmove):
    if depth == maxdepth:          # max depth reached, return a numerical value
        return evaluation(board)
    initial_board = copyboard(board)
    if level == 1:      # max level
        max = -99999
        successors = successor_func(board,1)
        for successor in successors:
            update_board(board, 1, successor)
            temp = minmax(depth+1, maxdepth, 0, board, nextmove)
            board = copyboard(initial_board)
            if max < temp:
                max = temp
                nextmove = successor
        return max, nextmove

    if level == 0:      # min level
        min = 99999
        successors = successor_func(board, 2)
        for successor in successors:
            update_board(board, 2,successor)
            temp = minmax(depth+1, maxdepth, 1, board, nextmove)
            board = copyboard(initial_board)
            if min > temp:
                nextmove = successor
                min = temp
        return min, nextmove

def grid_initialize():
    grid = [[0 for j in range(8)] for i in range(8)]
    grid[3][3] = 1
    grid[3][4] = 2
    grid[4][3] = 2
    grid[4][4] = 1
    return grid

def init_game_win():
    win = GraphWin("Othello", 80 * 8, 80 * 8)  # Create a window
    win.setBackground(color_rgb(0, 150, 100))

    msg = Text(Point(320, 300), "Choose Difficulty")
    msg2 = Text(Point(320, 320), "Easy")
    msg3 = Text(Point(320, 340), "Hard")
    msg.draw(win)
    msg2.draw(win)
    msg3.draw(win)
    win.getMouse()



def init_game_window():
    win = GraphWin("Othello", 80*8, 80*8)          # Create a window
    win.setBackground(color_rgb(0, 150, 100))

    # Draw grid
    for i in range(0, 8):
        for j in range(0, 8):
            p1 = Point(j*80, i*80)
            p2 = Point((j+1)*80, (i+1)*80)
            rec = Rectangle(p1, p2)             # Takes opposite points as input
            rec.draw(win)

    p3 = Point(3*80+40, 3*80+40)
    cir = Circle(p3, 20)
    cir.setFill(color_rgb(0, 0, 0))
    cir.draw(win)

    p3 = Point(3*80+40, 4*80+40)
    cir = Circle(p3, 20)
    cir.setFill(color_rgb(255, 255, 255))
    cir.draw(win)

    p3 = Point(4*80+40, 4*80+40)
    cir = Circle(p3, 20)
    cir.setFill(color_rgb(0, 0, 0))
    cir.draw(win)

    p3 = Point(4*80+40, 3*80+40)
    cir = Circle(p3, 20)
    cir.setFill(color_rgb(255, 255, 255))
    cir.draw(win)

    return win



def drawcircle(win,board):
    p = win.getMouse()
    x = p.getX()
    y = p.getY()

    p2d = Point(int(x/80) * 80 + 40, int(y/80) * 80 + 40)
    cir = Circle(p2d, 20)
    cir.setFill('white')
    cir.draw(win)
    upos= point(int(y/80), int(x/80))
    update_board(board,2,upos)
    return board;
def drawpossiblepositions(win, successors):
    for i in range(len(successors)):
        p2d = Point(successors[i].col * 80 + 40, successors[i].row* 80 + 40)
        cir = Circle(p2d,20)
        cir.draw(win)

def possiblepositions(board,win):
    successors = successor_func(board,2)
    drawcircle(win, successors)

def update_board_window(win,board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                p2d = Point(j * 80 + 40, i * 80 + 40)
                cir = Circle(p2d,20)
                cir.setFill("black")
                cir.draw(win)
            elif board[i][j] == 2:
                p2d = Point(j * 80 + 40, i * 80 + 40)
                cir = Circle(p2d, 20)
                cir.setFill("white")
                cir.draw(win)
            else:
                p2d = Point(j * 80 + 40, i * 80 + 40)
                cir = Circle(p2d, 20)
                cir.setFill(color_rgb(0,150,100))
                cir.setOutline(color_rgb(0,150,100))
                cir.draw(win)

def copyboard(board):
    tempboard = [[0 for j in range(8)] for i in range(8)]
    for i in range(8):
        for j in range(8):
            tempboard[i][j] = board[i][j]
    return tempboard