"""
Given a dictionary of distinct words and an M x N board where every cell has one character. Find all possible words
from the dictionary that can be formed by a sequence of adjacent characters on the board. We can move to any of 8
adjacent characters

Note: While forming a word we can move to any of the 8 adjacent cells. A cell can be used only once in one word.

"""

"""
Given inputs
N: number of words in the dict
dict: a set of words
Matrix: row X column dimensions
board: with row by column
    0      1      2      3
0 X1,Y1  X1,Y2  X1,Y3  X1,Y4
1 X2,Y1  X2,Y2  X2,Y3  X2,Y4
2 X3,Y1  X3,Y2  X3,Y3  X3,Y4
3 X4,Y1  X4,Y2  X4,Y3  X4,Y4

"""

"""
Steps
1. Define directions we can traverse for rows and columns
2. Define a function isValid: define a function to check if it is valid to move to a cell
3. Define a recursive function to get all possible words from the matrix with parameters (matrix, words, result, processed, i, j, path)
3a. set first position of the matrix (matrix[i][j]) as processed
3b. update the path with the value of the first value which was set to true
3c. check if the opath is in the words, if yes add the path(word to the result set)
3d. else, check for all possible movements


row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]
So, from position (x, y), we can move to:
 
(x – 1, y – 1) : NW
(x – 1, y)     : N
(x – 1, y + 1) : NE
(x, y – 1)     : W
(x, y + 1)     : E
(x + 1, y – 1) : SW
(x + 1, y)     : S
(x + 1, y + 1) : SE
"""


row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# define a function to check if it is valid to move to a cell
def isValid(x, y, processed):
    if 0 <= x < len(processed) and 0 <= y < len(processed[0]) and not processed[x][y]:
        return True


# define a recursive function to generate all words in a boggle
def searchBoggle(matrix, words, result, processed, i, j, path=''):
    # mark current node as processed
    processed[i][j] = True

    # update the path with the current character and insert it into the set
    path += matrix[i][j]

    # check whether the path is in the input set
    if path in words:
        result.add(path)

    # check for all 8 possible movements from the current cell
    for k in range(len(row)):
        # skip if a cell is invalid, or already processed
        if isValid(i + row[k], j + col[k], processed):
            searchBoggle(matrix, words, result, processed, i + row[k], j + col[k], path)

    # backtrack: mark the current node as unprocessed
    processed[i][j] = False


def searchInBoggle(matrix, words):
    # construct a set to store valid words constructed from the boggle
    result = set()

    # base case
    if not matrix or not len(matrix):
        return

    # `M X N` matrix
    (M, N) = (len(matrix), len(matrix[0]))

    # construct a boolean matrix to store whether a cell is processed or not
    processed = [[False for x in range(N)] for y in range(M)]

    # generate all possible words in a boggle
    for i in range(M):
        for j in range(N):
            # consider each character as starting point and run DFS
            searchBoggle(matrix, words, result, processed, i, j)

    return result


if __name__ == '__main__':
    board = [
        ['M', 'S', 'E'],
        ['R', 'A', 'T'],
        ['L', 'O', 'N']
    ]

    dicto = ['STAR', 'NOTE', 'SAND', 'STONE']

    valid_words = searchInBoggle(board, dicto)
    print(valid_words)
