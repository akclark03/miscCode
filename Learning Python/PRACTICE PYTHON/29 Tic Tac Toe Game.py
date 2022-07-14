# The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in this exercise is to use the functions from those previous
# exercises all together in the same program to make a two-player game that you can play with a friend.
# There are a lot of choices you will have to make when completing this exercise, so you can go as far or as little as you want with it.

# Here are a few things to keep in mind:

# You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
# If there are no more moves left, don’t ask for the next player’s move!
# As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.

import numpy as np
import time

def TicTacToe():
    game = np.full(9,0).reshape((3,3))

    def drawBoard(game):
        across = '\n --- --- ---\n'
        down = '|   '
        down1 = '| X '
        down2 = '| O '
        board = [across]

        for row in game:
            for i in row:
                if i == 0:
                    board.append(down)
                if i == 1:
                    board.append(down1)
                if i == 2:
                    board.append(down2)
            board.append('|')
            board.append(across)

        board.append('\n')
        for i in board:
            print(i, end="")

    def editBoard(plr,row,col):
        row -= 1
        col -= 1
        
        while True:
            if game[row][col] == 0:
                if plr == 1:
                    game[row][col] = 1
                if plr == 2:
                    game[row][col] = 2
                break
            else:
                return False

    def checkWinner(game):    
        # Check horizontal
        for row in game:
            rowValues = []
            for i in row:
                rowValues.append(i)
            if rowValues.count(1) == 3:
                return 1
            elif rowValues.count(2) == 3:
                return 2
        # Check vertical
        for i in range(3):
            columnValues = []
            for row in game:
                columnValues.append(row[i])
            if columnValues.count(1) == 3:
                return 1
            elif columnValues.count(2) == 3:
                return 2
        # Check Diagonal
        if game[0][0] == game[1][1] == game[2][2] == 1  or game[0][2] == game[1][1] == game[2][0] == 1:
            return 1
        if game[0][0] == game[1][1] == game[2][2] == 2  or game[0][2] == game[1][1] == game[2][0] == 2:
            return 2
            

    def playGame(game):
        player = 1

        while True:
            gameValues = set()
            for row in game:
                for i in row:
                    gameValues.add(i)

            if 0 in gameValues:
                time.sleep(2)
                if player == 1:
                    print('Player 1\'s turn:')
                    player += 1
                    if editBoard(1, int(input('Row: ')), int(input('Column: '))) == False:
                        time.sleep(1)
                        print('\nPlease choose an empty space on the Board.\n')
                        player = 1
                        continue
                    drawBoard(game)
                    if checkWinner(game) == 1:
                        print('Player 1 Wins!')
                        return 1
                
                elif player == 2:
                    print('Player 2\'s turn:')
                    player -= 1
                    if editBoard(2, int(input('Row: ')), int(input('Column: '))) == False:
                        print('Please choose an empty space on the Board.')
                        player = 2
                    drawBoard(game)
                    if checkWinner(game) == 2:
                        print('Player 2 Wins!')
                        return 2
            elif 0 not in gameValues:
                print('Board is Full! No Winner.')
                break
            
    print('''
    o---------- Welcome to TicTacToe! ----------o
    
    Player 1 will be X's, Player 2 will be O's.
    
    You place your marker on an empty space by indicating the Row and Column numbers.

    Player 1 will start first.
    ''')

    plr1Wins = 0
    plr2Wins = 0
    time.sleep(3)
    while True:
        game = np.full(9,0).reshape((3,3))
        drawBoard(game)

        outcome = playGame(game)

        if outcome == 1:
            plr1Wins += 1
        elif outcome == 2:
            plr2wins += 1
        
        time.sleep(2)
        ask = input('Would you like to play again? y/N: ')
        if ask.lower() == 'y':
            continue
        if ask.lower() == 'n':
            time.sleep(1)
            print('\nPlayer 1 finshed with '+str(plr1Wins)+' win(s),')
            print('Player 2 finished with '+str(plr2Wins)+' win(s)!\n')
            time.sleep(1)
            if plr1Wins > plr2Wins:
                print('Player 1 is the ulimate winner!')
                break
            elif plr1Wins < plr2Wins:
                print('Player 2 is the ultimate winner!')
                break
            else:
                print('It was a tie in the long run!')
                break

TicTacToe()