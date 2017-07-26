import collections
import time
"""
Finds the longest, second-longest, and total number of words from a text file
made up entirely of other words in the file concatenated together.
"""

def main():
    """
    MAIN function that opens and reads the file, splits its contents into WORDS,
    then prints the solution found by calling concatSearch(WORDS).
    OUTPUT (on separate lines):
        1. Longest concatenated word
        2. Second-longest concatenated word
        3. Total number of concatenated words.
        4. Total runtime (in seconds)
    """
    startTime = time.time()
    file_object = open('wordsforproblem.txt')
    words = file_object.read().split()
    file_object.close()
    results = concatSearch(words)

    print("Longest concatenated word: " + results[0])
    print("Second-longest concatenated word: " + results[1])
    print("Number of concatenated words: " + str(results[2]))
    finishTime = time.time() - startTime
    print("Total runtime (seconds): " + str(finishTime))

def getPrefixes(word, completedWords):
    """
    Return a list of words previously added to COMPLETEDWORDS that are valid
    prefixes (at the beginning) of WORD.
    """
    prefix = ''
    prefixes = []
    subWord = ""
    for letter in word:
        subWord += letter
        if subWord in completedWords:
            prefixes.append(subWord)
    return prefixes

def concatSearch(words):
    """
    Return a tuple containing the longest concatenated word, the second-longest
    concatenated word, and the total number of concatenated words.
    Algorithm:
    1. For each word, find all valid prefixes using getPrefixes(WORDS), then
        add the word to the COMPLETEDWORDS set.
    2. For each valid prefix found, add remaining suffix (word without prefix)
        and its original word as a tuple to the queue SUFFIXESREMAINING.
    3. After the first pass through WORDS, repeat steps 1 and 2 for every
        element (SUFFIX) in SUFFIXESREMAINING.
    4. Each time a word's SUFFIX is found in COMPLETEDWORDS, the word is a valid
        concatenated word; increment the CONCATWORDCOUNT and update the longest
        valid concatenated words so far. Otherwise, repeat.
    """
    longestWord = ''
    secondLongestWord = ''
    concatWordCount = 0
    concatWords = {""}
    suffixesRemaining = collections.deque()
    completedWords = {""}

    for word in words:
        prefixes = getPrefixes(word, completedWords)
        for prefix in prefixes:
            suffixesRemaining.append((word, word[len(prefix):]))
        completedWords.add(word)

    while suffixesRemaining:
        word, suffix = suffixesRemaining.popleft()
        if suffix in completedWords:
            if word not in concatWords:
                concatWords.add(word)
                concatWordCount += 1
            if len(word) > len(longestWord):
                secondLongestWord = longestWord
                longestWord=word
        else:
            prefixes = getPrefixes(suffix, completedWords)
            for prefix in prefixes:
                suffixesRemaining.append((word, suffix[len(prefix):]))

    return longestWord, secondLongestWord, concatWordCount

#Call to main function.
if __name__ == "__main__":
    main()
