# Modify the code below:
"""
Modify the sentence-generator program so that it inputs its vocabulary from a set of text files at startup.
The filenames are nouns.txt, verbs. txt, articles.txt, and prepositions.txt.

- This function should expect a filename as an argument.
- The function should open an input file with this name, define a temporary list,
    read words from the file, and add them to the list.
- The function should then convert the list to a tuple and return this tuple
- Call the function with an actual filename to initialize each of the four variables for the vocabulary.)

example:
Enter the number of sentences: 1

THE GIRL SAW THE BALL BY THE BALL
"""

import random

# added the getWords method
def getWords(filename):
    readFile = open(filename, 'r')  # open the file
    templist = list()  # declare a temporary list
    for line in readFile:  # read through the loop
        line = line.strip()
        templist.append(line)  # add to the temporary list
    allwords = tuple(templist)  # convert the list into a tuple
    readFile.close()  # close the file
    return allwords  # return all the words

articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()


def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)


def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()


def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()


def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


# The entry point for program execution
if __name__ == "__main__":
    main()
