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
                    white, black = ballcount(board)
                    if white > black:
                        text = Text(Point(725, 300), "Human Wins")
                        text.setSize(18)
                        text.setStyle("bold italic")
                        text.draw(win)
                        break
                    elif black > white:
                        text = Text(Point(725, 300), "Computer Wins")
                        text.setSize(18)
                        text.setStyle("bold italic")
                        text.draw(win)
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
                    text = Text(Point(725,300), "Human Wins")
                    text.setSize(18)
                    text.setStyle("bold italic")
                    text.draw(win)
                    break
                elif black > white:
                    text = Text(Point(725, 300), "Computer Wins")
                    text.setSize(18)
                    text.setStyle("bold italic")
                    text.draw(win)

                break
            board = copyboard(tempboard)
            update_board(board,player,nextCPUmove)
            update_window(win,board)
            player = 2
    win.getKey()
    win.close()



__main__()