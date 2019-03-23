#LISTS (29PTS TOTAL)
#In these exercises you should should use functions as needed.  All functions should have comments to describe their purpose.

import random
import time
# PROBLEM 1 (Using List Comprehensions - 6pts)
# Use the list comprehension method to do the following:
# a) Make a list of numbers from 1 to 100
# b) Make a list of even numbers from 20 to 40
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)


# Part A
a_list = [x for x in range(101)]
print(a_list)
print()
# Part B
b_list = [y for y in range(20, 41) if y % 2 == 0]
print(b_list)
print()
# Part C
c_list = [x ** 2 for x in range(101)]
print(c_list)
print()
print()



#PROBLEM 2 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
import random

answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

random_word = answer_list.pop(random.randrange(len(answer_list)))
print("Ask me a question about your future: ")
print(random_word)
print()

# PROBLEM 3 (Shuffle - 8pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order. Print the random deck. 
# Then deal yourself a hand of 5 cards off the top.  Print the hand.  Print the remaining deck.


suits = ["S", "C", "H", "D"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]




def shuffle(deck):
    new_deck = []
    while len(deck) > 0:
        card = deck.pop(random.randrange(len(deck)))
        new_deck.append(card)
    return new_deck

deck = []
for card in cards:
    for suit in suits:
        deck.append(card + suit)

print(deck)

new_deck = shuffle(deck)
print(new_deck)
print(len(new_deck))

deal = new_deck[0:5]
print(deal)
print()

# PROBLEM 4 (Illinois Pick 4 - 10pts)
# Lotteries are known to give awful odds of winning, and incredibly low expected returns on your invevestment.
# You will buy 10000 Illinois Pick 4 tickets in a simulation.
# Make a 2d lists of your picks.  Each number is a random 0 to 9.
# After you have made a list of 10000 lists (each 4 long), you will draw the official numbers
# After drawing the official numbers, you will go back through your list and check to see how many wins you got.
# The numbers must be an exact match in the exact position.
# Each ticket is $1.  If you win, you get $5000.  Simulate spending $10,000 on Pick 4 tickets, and see your return.

import random

list = [[random.randrange(10), random.randrange(10), random.randrange(10), random.randrange(10)] for x in range(1000)]
print(list)
main_list = [random.randrange(10), random.randrange(10), random.randrange(10), random.randrange(10)]
wins = 0
for i in range(len(list)):
    if main_list[0] == list[i][0] and main_list[1] == list[i][1] and main_list[2] == list[i][2] and main_list[3] == list[i][3]:
        wins += 1
print(main_list)
print("You won", wins, "times.")
list = [[random.randrange(10), random.randrange(10), random.randrange(10), random.randrange(10)] for x in range(10000)]
money = 0
for i in range(len(list)):
    money -= 1
    if main_list[0] == list[i][0] and main_list[1] == list[i][1] and main_list[2] == list[i][2] and main_list[3] == list[i][3]:
        wins += 1
        money += 5000

if money > 0:
    print("You made", money, "dollars.")
elif money == 0:
    print("You broke even.")
else:
    print("You have", money, "dollars. ):")