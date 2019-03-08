'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

import re
dictionary_list = []
index = 0
longest_length = 0

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open('dictionary.txt', 'r')
with open('dictionary.txt') as word:
    list = [x.strip() for x in word]

for i in range(len(list)):
    if len(list[i]) > longest_length: # this says that if the word being looked at is bigger than all previous ones than...
        longest_length = len(list[i])
        longest_word = list[i]
        index = i # I can't figure out how to print the letter represented by the number
print("Longest word is", longest_length)

file.close()


#2.  (8pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"

length_list = []

file = open('AliceInWonderLand.txt')
number = 0
average = 0
for line in file:
    line = line.strip()
    words = split_line(line)
    for letter in words:
        number += 1
        letter_2 = len(letter)
        length_list.append(letter_2)

total = sum(length_list)

print("The average word is", (total / number), "letters")
print("The total numnber of words is:", number)



# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (12pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?





#### OR #####

#3  (12pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

file = open('AliceInWonderLand.txt')
alice = []

for line in file:
    line = line.strip()
    words = split_line(line)
    for word in words:
        alice.append(word)

seven_letters = []
for i in alice:
    if len(i) == 7:
        seven_letters.append(i)
seven = []
for i in seven_letters:
    seven.append(seven_letters.count(i))

most = seven_letters[seven.index(max(seven))]
print("The most commonly occurring 7 letter word is: ", most.upper())


# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



