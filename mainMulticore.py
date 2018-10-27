from multiprocessing import Pool
import itertools

class WordSearch(object):
    def __init__(self, grid):
        self.grid = grid
        self.ROW_LENGTH = len(grid)

    # The 'direction' variable represents either top to bottom (0) or left to right (1)
    def searchWordInGrid(self, word, i, j, direction):
        # Recursive heap approach
        # Return true if word is empty
        if len(word) == 0:
            return True

        # If out of bounds
        if i >= self.ROW_LENGTH or j >= self.ROW_LENGTH:
            return False

        # Check if first character is the same as the word's first character
        if grid[i][j] is not word[0]:
            return False
        if direction == 0:
            i += 1
        else:
            j += 1
        word = word[1:]

        # Return true if word is empty
        if len(word) == 0:
            return True

        # Optimisation to reduce the number of full word searches by also checking the last character of the string
        # Check if indexes won't get out of bounds
        if direction == 0:
            oob = i + len(word) - 1 >= self.ROW_LENGTH
        else:
            oob = j + len(word) - 1 >= self.ROW_LENGTH

        if oob is True:
            return False

        # Now check if the last character of the word appears either at the bottom, or right relative to the start of the word in the grid
        i_end = True
        j_end = True
        if direction == 0:
            i_end = grid[i+len(word)-1][j] is word[len(word)-1]
        else:
            j_end = grid[i][j+len(word)-1] is word[len(word)-1]

        if i_end is False or j_end is False:
            return False
        word = word[:-1]

        # Now calculate the middle of the word
        mid = len(word)/2
        if len(word)%2 == 1:
            addCoord = int(mid - 0.5)
        else:
            addCoord = int(mid)

        # Finally return the same method call for the first half and second half from both top to bottom and left to right
        if direction == 0:
            return (self.searchWordInGrid(word[:int(mid)], i, j, direction)
                    and self.searchWordInGrid(word[int(mid):], i + addCoord, j, direction)
                )
        else:
            return (self.searchWordInGrid(word[:int(mid)], i, j, direction)
                    and self.searchWordInGrid(word[int(mid):], i, j + addCoord, direction)
                )


    def wordPresent(self, params):
        i, j, word = params
        if self.searchWordInGrid(word, i, j, 0) is True or self.searchWordInGrid(word, i, j, 1) is True:
            return True
        return False

    def is_present(self, word):
        # For each coordinates i and j in the grid, check if the word exists
        for i in range(self.ROW_LENGTH):
            for j in range(self.ROW_LENGTH):
                params = i, j, word
                
                if self.wordPresent(params) is True:
                    return True
        return False


# Create method to generate a random grid
import string, random

def random_grid(LEN):
    a = [[0 for x in range(LEN)] for y in range(LEN)]
    for i in range(LEN):
        for j in range(LEN):
            a[i][j] = random.choice(string.ascii_uppercase)
    return a


# Defining grid to check and words to find

words_to_find = ['DINOSAUR', 'YES', 'PEXIP', 'IS', 'SO', 'COOL']
grid = random_grid(1000)


# Testing the code

# all_words = [line.rstrip('\n').replace("\'", '').upper() for line in open('/usr/share/dict/words')]

ws = WordSearch(grid)

for word in words_to_find:
    if ws.is_present(word):
        print("found {}".format(word))