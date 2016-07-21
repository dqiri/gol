import time
gameboard = [[' ' for __ in xrange(10)] for __ in xrange(10)]

def update(board):
    for row in xrange(len(board)):
        for col in xrange(len(board[row])):
            cell = board[row][col]

            neighbors = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
            xtally = 0
            for i, j in neighbors:
                if i >= 0 and i < len(board):
                    if j >= 0 and j < len(board[row]):
                        if board[i][j] == 'x' or board[i][j] == 'Dead':
                            xtally += 1
            if cell != 'x':
                if xtally == 3:
                    board[row][col] = 'Alive'
            else:
                if xtally < 2:
                    board[row][col] = 'Dead'
                if xtally > 3:
                    board[row][col] = 'Dead'

    for row in xrange(len(board)):
        for col in xrange(len(board[row])):
            if board[row][col] == 'Dead':
                board[row][col] = ' '
            if board[row][col] == 'Alive':
                board[row][col] = 'x'

def game_print(board):
    for row in board:
        print '|' + '|'.join(row) + '|'


gameboard[4][4] = 'x'
gameboard[4][5] = 'x'
gameboard[3][4] = 'x'
gameboard[1][4] = 'x'


game_print(gameboard)
update(gameboard)
time.sleep(3)
game_print(gameboard)
update(gameboard)
time.sleep(3)

game_print(gameboard)
update(gameboard)
time.sleep(3)
game_print(gameboard)
update(gameboard)
time.sleep(3)
