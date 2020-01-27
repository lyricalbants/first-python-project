# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 09:26:15 2020

@author: Emmanuel Ezeobidi

### Milestone Project: Create a Tic-tac-toe game
"""
#import module
from IPython.display import clear_output
import time

#game start
def start_game():
    
    #board to save players' markers
    mainboard = [" " for x in range(10)]
    board = mainboard
    
    #print interface
    def printTitle():
        print(" X | O | X ")
        print("--- --- ---")
        print(" O | X | O ")
        print("--- --- ---")
        print(" X | O | X ")
        print("TO PLAY TIC - TAC - TOE, \n YOU NEED TO GET THREE IN A ROW.\n \
              YOUR CHOICES ARE BETWEEN 1 TO 9.")
        clear_output(wait=True)
    
    #print board
    def printBoard():
        print ( "   |   |   ")
        print (" "+board[1]+" | "+board[2]+" | "+board[3]+"  ")
        print ("   |   |")
        print ("---|---|---")
        print ("   |   |")
        print (" "+board[4]+" | "+board[5]+" | "+board[6]+"  ")
        print ("   |   |")
        print ("---|---|---")
        print ("   |   |")
        print (" "+board[7]+" | "+board[8]+" | "+board[9]+"  ")
        print ("   |   |   ")
    
    
    #store players' input
    def store(p_marker, p_index):
        
        while board[p_index] in ["X", "O"]:
            print("Position already taken, pick another")
            p_index = lambda: int(input("Enter a different number: "))
            p_index = p_index()
            if board[p_index] == " ":
                board[p_index] = p_marker
                break
        
        
        else:
            board[p_index] = p_marker
    
    
    
    # check marker for win or tie after board is full
    def check_for_win(p_marker):
        if board[1]==board[2]==board[3] == p_marker:
            return "Game over" 
        elif board[4]==board[5]==board[6] == p_marker:
            return "Game over"
        elif board[7]==board[8]==board[9] == p_marker:
            return "Game over"
        elif [board[1], board[4], board[7]].count(p_marker) == 3:
            return "Game over"
        elif [board[2], board[5], board[8]].count(p_marker) == 3:
            return "Game over"
        elif [board[3], board[6], board[9]].count(p_marker) == 3:
            return "Game over"
        elif [board[1], board[5], board[9]].count(p_marker) == 3:
            return "Game over"
        elif [board[3], board[5], board[7]].count(p_marker) == 3:
            return "Game over"
    
    
    
    #welcome players to the game
    print("Welcome, battle-hardened warriors!")
    printTitle()
    
    
    #player one
    p1_marker = "X"
    p1_index = lambda: int(input("Player 1, Enter position of markers in \
                                 numbers, 1 - 9: "))
    
    #player two
    p2_marker = "O"
    p2_index = lambda: int(input("player 2, Enter position of markers in \
                                 numbers, 1 - 9: "))
    
    
    
    while " " in board[1:]:
        clear_output(wait=True)
        
        
        #player 1 turn
        store(p1_marker, p1_index())         
        printBoard()     
        if check_for_win(p1_marker) == "Game over":
            print("Player one wins")
            break
        elif " " not in board[1:]:
            break
        
        #player 2 turn
        store(p2_marker, p2_index())            
        printBoard()
        if check_for_win(p2_marker) == "Game over":
            print("Player two wins")
            break
        elif " " not in board[1:]:
            break
    
    #check for draw
    if check_for_win(p1_marker) != "Game over" \
        and check_for_win(p2_marker) != "Game over":
            print("Game tied, there is no winner!")
    
    
    #action after game ends, replay or end game!
    time.sleep(1)
    replay = input("Do you want to replay, y/n: ")
    board = mainboard
    if replay == "n":
        return "Game Over!"
    start_game()

start_game()









