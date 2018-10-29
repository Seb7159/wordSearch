from WordSearchMultiprocess import WordSearch

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

# Benchmarking
import time
t = time.time()

for word in words_to_find:
    # t1 = time.time()
    if ws.is_present(word):
        print("found {}".format(word))
    # print(word, time.time() - t1)

print("Took ", time.time() - t, " seconds to find all words. ")