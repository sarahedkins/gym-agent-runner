import math
from string import ascii_lowercase

alphabet = "_" + ascii_lowercase

def word_to_state(word):
    state = 0
    for place, char in enumerate(word):
        state += alphabet.index(char) * ( 27 ** (len(word) - 1 - place) )
    return state

def state_to_word(state_id, word_length):
    word = ""
    for i in range(0, word_length):
        m = state_id  / ( 27 ** i )
        idx = math.floor(m)
        word = alphabet[idx % 27] + word
    return word

def get_all_states(n):
    words = []
    for i in range(0, 27 ** n):
        words.append(state_to_word(i, n))
    return words
