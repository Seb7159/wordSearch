# WordSearch class
class WordSearch(object):
    def __init__(self, grid):
        self.grid = grid
        self.ROW_LENGTH = len(grid)
        self.DIRECTION_X = [1, 0]
        self.DIRECTION_Y = [0, 1]

    def searchWordInGrid(self, word, i, j):
        # Check if first character is the same as the word's first character
        if grid[i][0][j] is not word[0]:
            return False
        # For each direction (from top to bottom, from left to right)
        for d in range(len(self.DIRECTION_X)):
            # Define temporary coordinates new_i, new_j, then a flag to check to word at the end
            new_i = i
            new_j = j
            flag = True
            # From the second character onwards, check if they correspond
            for k in range(1, len(word)):
                # Increment temporary coordinates
                new_i += self.DIRECTION_X[d]
                new_j += self.DIRECTION_Y[d]
                # In case temporary coordinates go out of bounds
                if new_i >= len(grid) or new_j >= len(grid):
                    flag = False
                    break
                # Check if they correspond
                if grid[new_i][0][new_j] is not word[k]:
                    flag = False
                    break
            # If the flag stood on True, it means the word has been found
            if flag is True:
                return True
        # If nothing has been found, return False
        return False


    def is_present(self, word):
        # For each coordinates i and j in the grid, check if the word exists
        for i in range(self.ROW_LENGTH):
            for j in range(self.ROW_LENGTH):
                if self.searchWordInGrid(word, i, j) is True:
                    return True
        return False


# Defining grid to check and words to find

words_to_find = ['DINOSAUR', 'YES', 'PEXIP', 'IS', 'SO', 'COOL']
grid = [
    ['PEXIPA'],
    ['ADSSOL'],
    ['CDOLSD'],
    ['OSADSA'],
    ['OKJBFK'],
    ['LSDASD']
]


# Testing the code

ws = WordSearch(grid)

for word in words_to_find:
    if ws.is_present(word):
        print("found {}".format(word))