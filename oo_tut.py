import time

class GameOfLife(object):
    def __init__(self, rows = 10, cols = 10):
        self.gameboard = [[' ' for __ in xrange(cols)] for __ in xrange(rows)]

    def update(self, board):
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
        self.game_print()

    def game_print(self):
        for row in self.gameboard:
            print '|' + '|'.join(row) + '|'

    def __repr__(self):
        strbuilder = ['|' + '|'.join(row) + '|' for row in self.gameboard]
        return '\n'.join(strbuilder)



x = GameOfLife(10, 10)

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
