import random


def drawboard(board):
    print('     |       ')
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
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Do you want to be X or O: ').upper()
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']


def who_play_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def play_again():
    print('Do you want to play again?(yes or No)')
    return input().upper().startwith('y')


def make_move(board, letter, move):
    board[move] = letter


def winner(bo, le):
    # return Boolean (true or false)
    return ((bo[7] == bo[8] == bo[9] == le) or  # across the top
            (bo[4] == bo[5] == bo[6] == le) or  # across the middle
            (bo[1] == bo[2] == bo[3] == le) or  # across the bottom
            (bo[7] == bo[4] == bo[1] == le) or  # down the left side
            (bo[8] == bo[5] == bo[2] == le) or  # down the middle
            # down the right side
            (bo[9] == bo[6] == bo[3] == le) or
            (bo[7] == bo[5] == bo[3] == le) or  # diagonal
            (bo[9] == bo[5] == bo[1] == le))


def getboardcopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard


def free_space(board, move):

    return board[move] == ' '


def getplayermove(board):
    move = ''
    while move not in '1,2,3,4,5,6,7,8,9'.split() or not free_space(board, int(move)):
        try:
            move = int(input("what is your next move?Choose(1-9)"))
        except:
            print("This is not a Valid number")


def random_move(board, moveList):
    possibleMoves = []
    # moveList is an integer
    for i in moveList:
        if free_space(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def computer_move(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1, 10):
        copy = getboardcopy(board)
        if free_space(copy, i):
            make_move(copy, computerLetter, i)
            if winner(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = getboardcopy(board)
        if free_space(copy, i):
            make_move(copy, playerLetter, i)
            if winner(copy, playerLetter):
                return i
    move = random_move(board, [1, 3, 7, 9])
    if move != None:
        return move

    if free_space(board, 5):
        return 5

    return random_move(board, [2, 4, 6, 8])


def board_full(board):
    for i in range(1, 10):
        if free_space(board, i):
            return False
        return True


print("Welcome to Smart tictactoe beat the Game!")
while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = player_input_letter()
    turn = who_play_first()
    print('The' + turn + 'will go first!')
    GameisOn = True

    while GameisOn:

        if turn == 'player':
            drawboard(theBoard)
            move = getplayermove(theBoard)
            make_move(theBoard, playerLetter, move)

            if winner(theBoard, playerLetter):
                drawboard(theBoard)
                print('Player wins Smart player')
                GameisOn = False
            else:
                if board_full(theBoard):
                    drawboard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            move = computer_move(theBoard, computerLetter)
            make_move(theBoard, computerLetter, move)

            if winner(theBoard, computerLetter):
                drawboard(theBoard)
                print('The computer has beaten you! You lose.')
                GameisOn = False
            else:
                if board_full(theBoard):
                    drawboard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not play_again():
        break
