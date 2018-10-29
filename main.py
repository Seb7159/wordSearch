from WordSearch import WordSearch

ROW_LENGTH = 1000
words_to_find = ['dinosaur', 'yes', 'pexip', 'is', 'so', 'cool']


# Create method to generate a random grid
import string, random

def random_grid(LEN):
    a = [[0 for x in range(LEN)] for y in range(LEN)]
    for i in range(LEN):
        for j in range(LEN):
            a[i][j] = random.choice(string.ascii_lowercase)
    return a

grid = random_grid(ROW_LENGTH)


# Start program

ws = WordSearch(grid)

# Benchmarking

import time
t = time.time()

# Start processing
for word in words_to_find:
    # t1 = time.time()
    if ws.is_present(word):
        print("found {}".format(word))
    # print(word, time.time() - t1)

print("Took ", time.time() - t, " seconds to find all words without multiprocessing. ")