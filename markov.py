#!/usr/bin/env python

import sys
<<<<<<< HEAD
from random import randint


def make_chains(corpus):
    """Takes an input text as a string and returns a dict of
    markov chains."""
    # return {}
    # Split text into list of words
    words = corpus.split()

    # Create an empty dict
    d = {}

    # Traverses list of words builds the dict
    for i in range(len(words) - 2):
        # Create tuple of a word and the following word as a key
        key = (words[i], words[i + 1])
        # Check to see if the tuple/key is in the dict
        if not d.get(key):
            # If it's not in the dict, add it as a new value list
            d[key] = [words[i + 2]]
        else:
            # If it's in the dict, append to values list
            d[key].append(words[i + 2])

    # for key in d:
    #     print "Key: %s,\t\t\tValue: %s" % (key, d[key])
    
    return d 

def make_text(chains):
    """Takes a dict of markov chains and returns random text
    based off an original text."""
    #return "Here's some random text."

    # Return a list of dict keys
    keys = chains.keys()

    words = []
    # Finding a capitalized word to start first tuple
    while len(words) == 0:   
        # Create a random number start to index into the list of keys
        start = randint(0, len(keys) - 1)

        # Pull random key from list of keys
        key = keys[start]

        # Make sure first item in first tuple is a capilized letter
        if key[0][0].capitalize() == key[0][0]: 
            words = [key[0], key[1]]
            # Same as:         
                # words = []
                # words.append(key[0])
                # words.append(key[1])

    # Getting the next word
    while chains.get(key) and len(words) < 25:
        # value = chains[key]
        # rand_number = randint(0, len(value) - 1)
        # rand_word = value[rand_number]
        rand_number = randint(0, len(chains[key]) - 1)
        rand_word = chains[key][rand_number]        

        # Append random word to words list value
        words.append(rand_word)

        # Updating key to be the last two items in list
        key = tuple((words[-2:]))

    end_punct = ".!?"
    # Keep going until we find a second tuple that ends in end_punct
    while chains.get(key) and end_punct.find(key[1][-1]) == -1:
        value = chains[key]
        rand_number = randint(0, len(value) - 1)
        rand_word = value[rand_number]

        words.append(rand_word)

        # Updating key to be the last two items in list
        key = tuple((words[-2:]))

    return ' '.join(words)

=======


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    input_textr = corpus.read()
    split_words = input_textr.split()

    split_word_dict = {}
    for word in split_words:
        if not split_word_dict.get(word):
            for index in range(len(split_words)-2):
        #if not split_word_dict.get(index):
            #If it's not in the dictionary, add two items from the list as keys and the next item as the value
        
            #split_word_dict[index] = split_word_dict[(split_words[index] , split_words[index + 1])] = [split_words[index + 2]]
        #else:
            #If the item is already in the dictionary as a key, we need to add the next two items to the key's values
            #split_word_dict[index].append(split_words[index + 2])
            #split_word_dict = {}
    #for index in range(len(split_words)-2):
                split_word_dict[(split_words[index] , split_words[index + 1])] = [split_words[index + 2]]
        else:
            split_word_dict[word].append(split_words[index + 2])
    print split_word_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."
>>>>>>> 9123f2b0f77f82721520d8348c370bd76f592779

def main():
    args = sys.argv

<<<<<<< HEAD
    script, filename1, filename2 = args

    f1 = open(filename1)
    f2 = open(filename2)
    input_text = f1.read()
    input_text += f2.read()
    f1.close()
    f2.close()
=======
    # Change this to read input_text from a file
    input_text = open('input_text.txt', 'r')

    # Data Structure
    # {(bigram_1, bigram_2): [unigram]}
>>>>>>> 9123f2b0f77f82721520d8348c370bd76f592779

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
