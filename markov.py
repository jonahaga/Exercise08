#!/usr/bin/env python

import sys


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

def main():
    args = sys.argv

    # Change this to read input_text from a file
    input_text = open('input_text.txt', 'r')

    # Data Structure
    # {(bigram_1, bigram_2): [unigram]}

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
