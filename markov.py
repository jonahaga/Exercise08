#!/usr/bin/env python

import sys


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    input_textr = corpus.read()
    split_words = input_textr.split()
    
    split_word_dict = {}
    for word in range(len(split_words)-2):
        split_word_dict[(split_words[word] , split_words[word + 1])] = [split_words[word + 2]]
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
