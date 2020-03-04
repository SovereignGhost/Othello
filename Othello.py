from HelperFunctions import *
import time


def __main__():
    board = grid_initialize()
    win  = init_game_window()
    maxdepth = 1;
    player = 2
    nextCPUmove = None
    while(1):

        if player == 2:
            successor = successor_func(board,player)
            drawpossiblepositions(win,successor)
            board = drawcircle(win,board)
            update_board_window(win,board)
            time.sleep(1)
            player = 1
        elif player == 1:
            tempboard = copyboard(board)
            max,nextCPUmove = minmax(0,1,1,board, nextCPUmove)
            board = copyboard(tempboard)
            update_board(board,player,nextCPUmove)
            update_board_window(win,board)
            player = 2



__main__()