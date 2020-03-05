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
                cpu_successors = successor_func(board,1)
                if len(cpu_successors) > 0:
                    player = 1
                else:
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
            if player == 2:
                drawpossiblepositions(win,successors)
                board, upos = drawcircle(win,board)
                update_window(win,board)
                cir = Circle(Point(upos.col * 80 + 40, upos.row * 80 + 40),5)
                cir.setFill("red")
                cir.draw(win)
                time.sleep(1)
                player = 1
        elif player == 1:
            tempboard = copyboard(board)
            temp, nextCPUmove = minmax(0,maxdepth,1,board)
            if nextCPUmove is None:
                human_successors = successor_func(board,2)
                if len(human_successors) > 0:
                    player = 2
                else:
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
            if player == 1:
                board = copyboard(tempboard)
                update_board(board,player,nextCPUmove)
                update_window(win,board)
                cir = Circle(Point(nextCPUmove.col * 80 + 40, nextCPUmove.row * 80 + 40), 5)
                cir.setFill("red")
                cir.draw(win)
                player = 2
    win.getKey()
    win.close()



__main__()