"""
This module takes all the contents from the 'words.txt' file, which contains the glossary of
words for this game.
Also, it contains functions to split them up into individual words, get random words. etc.
"""

import random


FILE_NAME = "E:\Programs & Codes\Python - 100 days of Python\hangman game\words.txt"

words_file = open(FILE_NAME, "r")

words = words_file.readlines()
words = [ word.strip() for word in words if len(word)>8 ]
# Can be used for debugging purposes
# print(words)

words_file.close()

def get_a_random_word():
    random_index = random.randint(0, len(words)-1)
    return words[random_index].upper()

print(get_a_random_word())