# Hangman code in python

import random
import os 

print(random.randint(3, 9))
with open(r"C:\Users\7flig\Downloads\words.txt",'r') as dict_file:
    words_file = dict_file.readlines()

rand_integer = random.randint(0,len(words_file))
word_selected = words_file[rand_integer].lower()


def dashes(word, guessedLetters : list):
    if len(guessedLetters) == 0:
        return list('*'*len(word))
    #[' {0} '.format(elem) for elem in lst]
    else: 
        stars = list('*'*len(word))
        indices = []
        for gl in guessedLetters:
            for al in range(len(word)):
                if gl == word[al]:
                    indices.append(al)
        for ind in indices:
            stars[ind] = word[ind]
        return stars


mistakes = 0 
letters = []
while True:
    os.system('cls')
    print('Guess a letter')
    print('You have 5 chances')
    print('Mistakes =', mistakes)
    print(dashes(word=word_selected, guessedLetters=letters))
    letter = input('Enter a letter: ')
    letters.append(letter)
    #print(dashes(word=word_selected, guessedLetters=letters))
    if word_selected.find(letter) <= 0:
        mistakes += 1
    if dashes(word=word_selected,guessedLetters=letters).count('*') == 0:
        print('You guess all the letters. Hurray')
    if mistakes >= 5:
        break 

print('The word was', word_selected)
print('Game Ended')
