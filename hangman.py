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

word_list = ["tennis", "soccer", "basketball", "squash", "golf", "track"]
wrong_number = 0
right_number = 0
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
    print(HANGMANPICS[wrong_number])
    for letter in letters_used:
        print(letter, end=" ")
    print()
    for letter in secret_word:
        if letter in letters_used:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
    guess = input("Chose a letter: ")
    if letter in secret_word:
        right_number += 1
        print(letter)
        if guess in letters_used:
            print("Already Used")
        else:
            letters_used.append(guess)
    if guess not in secret_word and letters_used:
        wrong_number += 1
        print(HANGMANPICS[wrong_number])
    if wrong_number >= 6:
        print("You are out of turns!")
        done = True
    if right_number == (len(secret_word)):
        print("Game Over. You won!")


# I need to say, "if letter in secret word then don't add 1 to guess number.
# This will then not add to picture if guess is correct and it will not count a correct guess as a turn.



