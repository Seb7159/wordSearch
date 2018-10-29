import multiprocessing

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
        if self.grid[i][j] is not word[0]:
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
            i_end = self.grid[i+len(word)-1][j] is word[len(word)-1]
        else:
            j_end = self.grid[i][j+len(word)-1] is word[len(word)-1]

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
            isPresent = True
            return True
        return False


    def is_present(self, word):
        # For each coordinates i and j in the grid, check if the word exists
        array = []
        for i in range(self.ROW_LENGTH):
            for j in range(self.ROW_LENGTH):
                params = i, j, word
                array.append(params)
        p = multiprocessing.Pool(processes=multiprocessing.cpu_count()-1)
        result = p.map(self.wordPresent, array)
        for n in result:
            if n is True:
                return True
        return False