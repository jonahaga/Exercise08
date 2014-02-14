#!/usr/bin/env python

import sys
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
        if ord(key[0][0]) >= ord('A') and ord(key[0][0]) <= ord('Z'):
            words = [key[0], key[1]]

    end_punct = ".!?"

    # Getting the next word
    while chains.get(key) and (len(' '.join(words)) < 25 or end_punct.find(key[1][-1]) == -1):
        rand_number = randint(0, len(chains[key]) - 1)
        rand_word = chains[key][rand_number]        

        # Append random word to words list value
        words.append(rand_word)

        # Updating key to be the last two items in list
        key = tuple((words[-2:]))

    sentence = ' '.join(words)
    return sentence

def valid_tweet(sentence):
    if len(sentence) < 140:
        return True
    else:
        return False


def main():
    args = sys.argv

    script, filename1, filename2 = args

    f1 = open(filename1)
    f2 = open(filename2)
    input_text = f1.read()
    input_text += f2.read()
    f1.close()
    f2.close()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    tweet = valid_tweet(random_text)

    while True:
        if tweet == False:
            random_text = make_text(chain_dict)
            tweet = valid_tweet(random_text)
        else:
            print random_text
            break


if __name__ == "__main__":
    main()