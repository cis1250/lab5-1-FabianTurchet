#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re
import string

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    sentence = input("Enter a sentence: ")
    while not is_sentence(sentence):
        print("This does not meet the criteria for a sentence.")
        sentence = input("Enter a sentence: ")
    return sentence

def calculate_frequencies(sentence):
    translator = str.maketrans("", "", string.punctuation)
    words = sentence.lower().translate(translator).split()

    word_list = []
    freq_list = []

    for w in words:
        if w in word_list:
            idx = word_list.index(w)
            freq_list[idx] += 1
        else:
            word_list.append(w)
            freq_list.append(1)
    return word_list, freq_list

def print_frequencies(words, freqs):
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {freqs[i]}")

def main():
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequencies(words, freqs)

main()
    
