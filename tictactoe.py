# Tic Tac Toe
'''
This is a demonstration of a simple AI coding
'''

import random


def drawboard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings
    # representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input_letter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first item,the computer's letter as the second.
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        letter = input('Do you want to be X or O: ').upper()

    # the first element in the list is the player’s letter,
    # the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_play_first():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def play_again():
    # This function returns True if the player wants to play again,
    # otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def make_move(board, letter, move):
    board[move] = letter


def winner(bo, le):
    return ((bo[7] == bo[8] == bo[9] == le) or  # across the top
            (bo[4] == bo[5] == bo[6] == le) or  # across the middle
            (bo[1] == bo[2] == bo[3] == le) or  # across the bottom
            (bo[7] == bo[4] == bo[1] == le) or  # down the left side
            (bo[8] == bo[5] == bo[2] == le) or  # down the middle
            # down the right side
            (bo[9] == bo[6] == bo[3] == le) or
            (bo[7] == bo[5] == bo[3] == le) or  # diagonal
            (bo[9] == bo[5] == bo[1] == le))

    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
 # diagonal


def getboardcopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def free_space(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


def getplayermove(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not free_space(board, int(move)):
        try:
            move = int(input("What is your next move? Choose(1-9)"))
            return move
        except:
            print("This is not a Valid number")


def random_move(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if free_space(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def computer_move(board, computerLetter):
    # Given a board and the computer's letter,
    # determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getboardcopy(board)
        if free_space(copy, i):
            make_move(copy, computerLetter, i)
            if winner(copy, computerLetter):
                return i

# Check if the player could win on their next move,
# and block them.
    for i in range(1, 10):
        copy = getboardcopy(board)
        if free_space(copy, i):
            make_move(copy, playerLetter, i)
            if winner(copy, playerLetter):
                return i

# Try to take one of the corners, if they are free.
    move = random_move(board, [1, 3, 7, 9])
    if move != None:
        return move

# Try to take the center, if it is free.
    if free_space(board, 5):
        return 5

# Move on one of the sides.
    return random_move(board, [2, 4, 6, 8])


def board_full(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if free_space(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = player_input_letter()
    turn = who_play_first()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player’s turn.
            drawboard(theBoard)
            move = getplayermove(theBoard)
            make_move(theBoard, playerLetter, move)

            if winner(theBoard, playerLetter):
                drawboard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if board_full(theBoard):
                    drawboard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer’s turn.
            move = computer_move(theBoard, computerLetter)
            make_move(theBoard, computerLetter, move)

            if winner(theBoard, computerLetter):
                drawboard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if board_full(theBoard):
                    drawboard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
