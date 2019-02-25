'''
Make a text based version of hangman (25pts)
Use the sample run as an example.  Try to make it as close as possible to the example. (or better)
'''

# PSEUDOCODE
# make a word list for your game
# grab a random word from your list and store it as a variable
# display the hangman
# display the used letters
# display the length of the word to the user using blank spaces
# prompt the user to guess a letter
# if the guess is correct increment correct_guesses by 1
# if the guess is incorrect increment incorrect_guesses by 1 and draw the next part of the hangman
# don't allow the user to select the same letter twice
# if the incorrect_guesses is greater than 6, tell the user they lost and exit the program
# if correct_guesses is equal to the length of the word, tell the user they won
# ask if they want to play again


# Feel free to use this list of ascii art for your game





import random

word_list = ["Tennis", "Soccer", "Basketball", "Squash", "Golf", "Track"]
guess_number = 0
secret_word = random.choice(word_list)
letters_used = []
guess = []

done = False

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


print("Welcome to Hangman")

while not done:
    print(HANGMANPICS[guess_number])
    for letter in letters_used:
        print(letter, end=" ")
    for letter in secret_word:
        if letter in letters_used:
            print("You already chose the letter.")
        if letter not in letters_used:
            print(letter, end=" ")
    print()
    guess = input("Chose a letter: ")
    if guess in letters_used:
        print("Already Used")
    else:
        letters_used.append(guess)
    if letter in secret_word:
        print(letter)
    else:
        guess_number += 1
    if guess_number >= 6:
        done = True







