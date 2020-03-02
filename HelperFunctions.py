# pointer class
class point:
    def __init__(self, rows, cols):
        self.row = rows
        self.col = cols

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
                if board[i-1][j] == ncolor and i >= 0:
                    temp = avail_post(board,color,"up",i-1,j)
                    if temp is not None and NotIn(retArr,temp):
                        retArr.append(temp)
                # check down
                if board[i+1][j] == ncolor and i < 8:
                    temp = avail_post(board,color,"down",i+1,j)
                    if temp is not None and NotIn(retArr,temp):
                        retArr.append(temp)
                # check right
                if board[i][j+1] == ncolor and i < 8:
                    temp = avail_post(board,color,"right",i,j+1)
                    if temp is not None and NotIn(retArr,temp):
                        retArr.append(temp)
                # check left
                if board[i][j-1] == ncolor and i >= 0:
                    temp = avail_post(board,color,"left",i,j-1)
                    if temp is not None and NotIn(retArr,temp):
                        retArr.append(temp)
                # check up-right
                if board[i-1][j+1] == ncolor and i >= 0 and j < 8:
                    temp = avail_post(board,color,"up-right",i-1,j+1)
                    if temp is not None and NotIn(retArr,temp):
                        retArr.append(temp)
                # check up-left
                if board[i-1][j-1] == ncolor and i >= 0 and j >= 0:
                    temp = avail_post(board,color,"up-left",i-1,j-1)
                    if temp is not None and NotIn(retArr,temp):
                        retArr.append(temp)
                # check down-right
                if board[i+1][j+1] == ncolor and i < 8 and j < 8:
                    temp = avail_post(board,color,"down-right",i+1,j+1)
                    if temp is not None and NotIn(retArr,temp):
                        retArr.append(temp)
                # check down-left
                if board[i+1][j-1] == ncolor and i < 8 and j >= 0:
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
    return black - white