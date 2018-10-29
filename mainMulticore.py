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

# Import the multiprocessing library and define the Pool p
import multiprocessing
p = multiprocessing.Pool(processes=multiprocessing.cpu_count() - 1)
result = p.map(ws.is_present, words_to_find)

# i represents the index of the array result and words_to_find
i = -1

# Start processing
for n in result:
    i += 1
    if n is True:
        print("found ", words_to_find[i])

print("Took ", time.time() - t, " seconds to find all words with multiprocessing. ")