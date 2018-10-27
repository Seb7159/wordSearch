# WordSearch class
class WordSearch(object):
    def __init__(self, grid):
        self.grid = grid
        self.ROW_LENGTH = len(grid)
        self.DIRECTION_X = [1, 0]
        self.DIRECTION_Y = [0, 1]

    def searchWordInGrid(self, word, i, j):
        # Recursive heap approach 
        # Return true if word is empty
        if len(word) == 0:
            return True

        # Check if first character is the same as the word's first character
        if grid[i][0][j] is not word[0]:
            return False
        i += 1
        word = word[1:]

        # Optimisation to reduce the number of full word searches by also checking the last character of the string
        # Check if indexes won't get out of bounds
        i_oob = i+len(word)-1 >= self.ROW_LENGTH
        j_oob = j+len(word)-1 >= self.ROW_LENGTH

        # Now check if the last character of the word appears either at the bottom, or right relative to the start of the word in the grid
        if i_oob is False:
            i_end = grid[i+len(word)-1][0][j] is not word[:-1]
        else:
            i_end = False

        if j_oob is False:
            j_end = grid[i][0][j+len(word)-1] is not word[:-1]
        else:
            j_end = False

        if i_end is False and j_end is False:
            return False
        j -= 1
        word = word[:-1]

        # If i overcomes or is equal to j, it means this is done
        if i >= j:
            return True

        # Now calculate the middle of the word
        mid = len(word)/2
        if len(word)%2 == 1:
            addCoord = int(mid+0.5)
        else:
            addCoord = int(mid)

        # Finally return the same method call for the first half and second half from both top to bottom and left to right
        return (self.searchWordInGrid(word[:int(mid)], i, j)
                and (
                        self.searchWordInGrid(word[int(mid):], i + addCoord, j)
                        or self.searchWordInGrid(word[int(mid):], i, j + addCoord)
                )
            )


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