# concatenated-words-challenge
When run from the command line (with "python WordsChallengeSolution.py"), my program prints to standard output:

Longest concatenated word: ethylenediaminetetraacetates
Second-longest concatenated word: electroencephalographically
Number of concatenated words: 97107

as well the runtime of the program in seconds (for timing purposes).

## About my approach:
My solution relies on the fact that each valid concatenated word contains at least another valid word as a prefix, at the beginning of the word (e.g. "applesauce" contains "apple" as its prefix). As the words in the file are parsed one-by-one and added to the "completedWords" set, we can assume that all valid prefixes of each word have already been previously added, since all the original words in the file are sorted lexicographically.

In my program's first pass through the words from the .txt file, all words with valid prefixes are identified, and for each prefix found the corresponding word is added as a double-ended queue (deque) along with the remainder of the word (suffix) without the prefix. After this first pass, the deque contains all words that could potentially be valid concatenated words. 

The program then iterates through the deque, repeating this "prefix-validation" process on each suffix. When a suffix is identified as a complete valid word, it is removed from the queue and its full original word is counted and compared to the longest concatenated word so far. Otherwise, it is checked for prefixes and re-added to the deque to continue the process.

The deque is eventually narrowed down until empty and returns the results to be printed.
