file = open("AliceInWonderLand200.txt")
import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

dictionary = []
for line in file:
    line = line.strip()
    words = split_line(line)
    dictionary.append(line)

file.close()


print ("\nLinear Search\n") # Why does it say every word is spelled wrong?

file = open("AliceInWonderLand200.txt")
line_number = 0

for line in file:
    line = line.strip()
    line_number += 1 # moves on to next line
    words = split_line(line)
    for word in words:
        wrong = 0
        while wrong < (len(dictionary)) != dictionary[wrong]: # might be the problem
            wrong += 1
        if wrong > len(dictionary) - 1:
            print("On Line", line_number, "misspelled word:", word)


line_number = 0
lower_pos = 0
upper_pos = len(dictionary)
found_pos = False
key = "Hello"


print("\nBinary Search\n")

for line in file:
    words = []
    line = split_line(line)
    words.append(line)
    for word in words:
        line_number += 1
        lower_pos = 0
        upper_pos = len(dictionary)
        found_pos = False
        key = word
        if word != (dictionary):
            print ("Line ",(line_number)," possible misspelled word: ",(word))

while lower_pos <= upper_pos and not found_pos:
    middle_pos = (upper_pos + lower_pos) // 2
    if dictionary[middle_pos] < key:
        lower_pos = middle_pos + 1
    elif dictionary[middle_pos] > key:
        upper_pos = middle_pos - 1
    else:
        found_pos = True

    if not found_pos:
        print("Line", line_number, "Possible incorrect spelling:", word)

file.close()
