# Concatenated Words challenge solution
I was fascinated by the variety of different approaches to a fun problem that I found online. However, after testing out some of the "fastest" optimized solutions on my own computer and seeing that most took around 5 to 10 seconds to run, I felt compelled to create a solution that could run in under 2 seconds.

I chose to attempt this with a very high-level programming language (Python) to see if I could keep my optimizations completely algorithmic, without relying on lower-level "hacks" that a compiled language like C would enable.


## The challenge
The challenge was to parse a file containing every single English word and find:
1. The longest "concatenated word" (a "concatenated word" being a word comprised entirely of other words in the file)
2. The second-longest "concatenated word"
3. The total number of all concatenated words

### Key points and assumptions (regarding the challenge):
- All words are lowercase and are SORTED.
- There are about 173,000 words total.
- Each word is listed on a new line, with no other whitespace.


## Running my solution
After downloading the files, navigate to the "concatenated-words-challenge" directory, and from there, run: 
'''
python WordsChallengeSolution.py
'''
My program prints to standard output:
- Longest concatenated word: ________________
- Second-longest concatenated word: _______________
- Number of concatenated words: _______________

as well the runtime of the program in seconds (for timing purposes).


## About my approach:
My solution relies on the fact that each valid concatenated word contains at least another valid word as a prefix, at the beginning of the word (e.g. "applesauce" contains "apple" as its prefix). As the words in the file are parsed one-by-one and added to the "completedWords" set, we can assume that all valid prefixes of each word have already been previously added, since all the original words in the file are sorted lexicographically.

In my program's first pass through the words from the .txt file, all words with valid prefixes are identified, and for each prefix found the corresponding word is added as a double-ended queue (deque) along with the remainder of the word (suffix) without the prefix. After this first pass, the deque contains all words that could potentially be valid concatenated words. 

The program then iterates through the deque, repeating this "prefix-validation" process on each suffix. When a suffix is identified as a complete valid word, it is removed from the queue and its full original word is counted and compared to the longest concatenated word so far. Otherwise, it is checked for prefixes and re-added to the deque to continue the process.

The deque is eventually narrowed down until empty and returns the results to be printed.

So... how did I do? Can you think of any other possible optimizations I may have overlooked? Feel free to let me know!
