"""Load a text file and strip it of whitespace
Get user input on how many letters after punctuation to look ahead and examine
Loop through number of letters from 1 to this lookahead value
    Start an empty string to hold the translation
    Start a counter
    Start a first-found marker and set to False
    Loop through characters in the text
        If character is punctuation
            Counter = 0
            First-found = True
        Otherwise, if first-found is True
            Counter + 1
        If counter = lookahead value
            Add character to translation string
    Display translation for this lookahead value
"""

import sys
import string

def load_text(file):
    # Load a text file as a string
    with open(file) as f:
        return f.read().strip()
    

def solve_null_cipher(message, lookahead):
    # Solve a null cipher based on number of letters after punctuation mark
    # message = null cipher text as a string stripped of whitespace
    # lookahead = endpoint of range of letters after punctuation mark to examine
    for i in range(1, lookahead + 1):
        plaintext = ''
        count = 0
        found_first = False
        for char in message:
            if char in string.punctuation:
                count = 0
                found_first = True
            elif found_first is True:
                count += 1
            if count == i:
                plaintext += char
        print(f"using offset of {i} after punctuation = {plaintext}")
        print()


        
