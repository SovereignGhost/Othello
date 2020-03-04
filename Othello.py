from HelperFunctions import *
import time


def __main__():
    board = grid_initialize()
    maxdepth, win = initialwindow()
    launch_game(win)
    player = 2
    nextCPUmove = point
    while(1):

        if player == 2:
            successors = successor_func(board,player)
            if len(successors) == 0:
                white, black = ballcount(board)
                if white > black:
                    print("Human Wins")
                    break
                elif black > white:
                    print("Computer Wins")
                    break
            drawpossiblepositions(win,successors)
            board = drawcircle(win,board)
            update_window(win,board)
            time.sleep(1)
            player = 1
        elif player == 1:
            tempboard = copyboard(board)
            temp, nextCPUmove = minmax(0,maxdepth,1,board)
            if nextCPUmove is None:
                white, black = ballcount(board)
                if white > black:
                    print("Human Wins")
                    break
                elif black > white:
                    print("Computer Wins")
                    break
            board = copyboard(tempboard)
            update_board(board,player,nextCPUmove)
            update_window(win,board)
            player = 2



__main__()