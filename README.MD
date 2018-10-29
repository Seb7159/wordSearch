# Word Search algorithm

This problem refers to a search algorithm applied in a two-dimensional grid for 
any given number of words. Given my the dimensions of the grid, that means we will have 
a complexity of at least O(n^2). On top of that, a word search would usually take 
an O(n) complexity, thus multiplied we would get to a complexity of O(n^3), which
would sounds like a pretty slow, but basic algorithm. 


## How to run 

To run this, either run main.py which will run the word search algorithm in a random grid
on a single processor. In order to run the same algorithm but with all except one processor,
you have to run mainMulticore.py. 

At the moment, the grid is set on a ROW_LENGTH of 1000 elements. To modify this, simply
edit the ROW_LENGTH variable at the start of each main files. 
(the reason why it is set on 1000 is because it takes around 1 second to run for the given words, 
whereas for 10^5 elements it would take around a minute)

To modify the words to search, edit the array called words_to_search at the 
start of both main files. 


## Efficiency 

The way this algorithm works in an efficient way is for the reason that the search
in the grid is based on a binary search, looking at the first and last characters of the word,
then recursively proceeding to check the first half, then the second half of the word.

This ensures a faster approach because many words can have the same start of the word (i.e.: 'addict' and 'addiction'), 
but in many cases, there is a small chance that words will have common start and end of characters;
and if they do, it will start to halven the word again and again until an agreement is reached.

The average case for this binary search algorithm is O(logn), but the worst case will be O(n).
For the whole algorithm in general of searching for a word in a two dimensional grid, 
the average case will be O(n^2logn) and worst case will be O(n^3).  


## Multiprocessing 

The multiprocessing part was created using the 'multiprocessing' library from Python 3.
The way it works is by allocating a word for each processor of the CPU except one for 
the better performance of the computer that is used. 

Each processor will find out if the word is in the grid or not. The tests results are listed below. 


### Tests

| Number of words 	| ROW_LENGTH 	| Single processing 	| Multiprocessing 	|
|-----------------	|:----------:	|-------------------	|-----------------	|
| 6               	| 10^2       	| 0.0468s           	| 0.0458s         	|
| 6               	| 10^3       	| 1.23s             	| 0.82s           	|
| 6               	| 10^4       	| 56.8995s          	| 66.9073s        	|

#### Interesting note
It is to be observed that for n = 10^4, single processing is faster than multiprocessing.
There may be various reasons why that happens which I still don't have an exact clue why that is.
A theory of mine would be the fact that the number of words is the same (6) for each case
and threads work asyncronously, thus it might make it slower. But I believe for a bigger 
number of words, the results would be better when using multiprocessing. 

#### CPU Used

Intel(R) Core(TM) i7-7500U CPU @ 2.70GHz (2 cores, 4 threads)

## Versions
Python 3.7 