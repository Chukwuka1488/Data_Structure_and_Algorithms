"""
Given an M × N matrix of characters, find the length of the longest path in the matrix starting from a given character. All characters in the longest path should be increasing and consecutive to each other in alphabetical order.

We are allowed to search the string in all eight possible directions, i.e., North, West, South, East, North-East, North-West, South-East, South-West.


For example, consider the following matrix of characters:
"""

# define directions
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# check if the direction to move from a point is valid
def isValid(x, y, mat):
    if 0 <= x < len(mat) and 0 <= y < len(mat[0]):
        return True


# The path should continue from the previous character.
# Here, (i, j) denotes the coordinates of the current cell.
def findNextCharacter(matrix, i, j, previous, path=''):
    # base case: return length 0 if the current cell (x, y) is invalid or
    # the current character is not consecutive to the previous character
    if not isValid(i, j, matrix) or chr(ord(previous) + 1) != matrix[i][j]:
        return

    path += matrix[i][j]

    # recur for all eight adjacent cells from the current cell
    for k in range(len(row)):
        # visit position (x + row[k], y + col[k]) and find the maximum length
        # from that path
        if isValid(i + row[k], j + col[k], matrix):
            findNextCharacter(matrix, i + row[k], j + col[k], matrix[i][j])

        # backtrack: mark the current node as unprocessed
        # processed[i][j] = False


def searchInBoggle(matrix, ch, path):
    # construct a set to store valid words constructed from the boggle
    # result = set()

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
            # start from the current cell if its value matches with the given character
            if matrix[i][j] == ch:
                # check for all 8 possible movements from the current cell
                for k in range(len(row)):
                    # recur for all eight adjacent cells from the current cell
                    if isValid(i + row[k], j + col[k], processed):
                        searchBoggle(matrix, words, processed, i + row[k], j + col[k], path)

                # backtrack: mark the current node as unprocessed
                processed[i][j] = False

                # consider each character as starting point and run DFS
                searchBoggle(matrix, words, processed, i, j)

    return len(path)
