#!/usr/bin/env python

import sys
import os
import twitter
from random import randint


def make_chains(corpus):
    """Takes an input text as a string and returns a dict of
    markov chains."""
    words = corpus.split()

    d = {}

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        if not d.get(key):
            d[key] = [words[i + 2]]
        else:
            d[key].append(words[i + 2])

    return d 

def make_text(chains):
    """Takes a dict of markov chains and returns random text
    based off an original text."""
    keys = chains.keys()
    words = []

    while len(words) == 0:   
        start = randint(0, len(keys) - 1)
        key = keys[start]

        if ord(key[0][0]) >= ord('A') and ord(key[0][0]) <= ord('Z'):
            words = [key[0], key[1]]

    end_punct = ".!?"

    while chains.get(key) and (len(' '.join(words)) < 25 or end_punct.find(key[1][-1]) == -1):
        rand_number = randint(0, len(chains[key]) - 1)
        rand_word = chains[key][rand_number]        

        words.append(rand_word)

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
    api = twitter.Api(consumer_key=os.environ.get("CONSUMER_KEY"), consumer_secret=os.environ.get("CONSUMER_SECRET"), access_token_key=os.environ.get("ACCESS_TOKEN"), access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET"))

    while True:
        if tweet == False:
            random_text = make_text(chain_dict)
            tweet = valid_tweet(random_text)
        else:
            api.PostUpdate(random_text)
            break


if __name__ == "__main__":
    main()