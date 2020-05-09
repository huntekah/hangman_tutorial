import random

def get_random_word():
    lines = open('polimorf_small.txt').read().splitlines()
    word = random.choice(lines).lower()
    return word
