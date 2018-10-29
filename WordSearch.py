# WordSearch class
class WordSearch(object):
    def __init__(self, grid):
        self.grid = grid
        self.ROW_LENGTH = len(grid)

    # Method to search a word in the grid
    # @param    self       the class
    # @param    word       word to be searched for
    # @param    i          the i index in the matrix
    # @param    j          the j index in the matrix
    # @param    direction  variable represents either top to bottom (0) or left to right (1)
    # @param    bool       return True if word is empty, False if conditions are not satisfied
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


    # Method of searching if word is present in grid
    # @param    self    the class
    # @param    word    the word to be searched for
    # @return   bool    True if found, False if not
    def is_present(self, word):
        # For each coordinates i and j in the grid, check if the word exists
        for i in range(self.ROW_LENGTH):
            for j in range(self.ROW_LENGTH):
                if self.searchWordInGrid(word, i, j, 0) is True or self.searchWordInGrid(word, i, j, 1) is True:
                    return True
        return False