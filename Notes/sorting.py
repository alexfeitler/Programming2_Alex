# sorting

# Swap Values
import random

a = 1
b = 2
print(a, b)


temp = a  # temporarily store one value before I overwrite
a = b
b = temp

print(a, b)

# pythonic way
a, b = b, a  # one line swap
print(a, b)

# Selection sort

# make a random list of 100 numbers from 1-99
rand_list = [random.randrange(1, 100) for x in range(100)]
print(rand_list)

for cur_pos in range(len(rand_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(rand_list)):
        if rand_list[scan_pos] < rand_list[min_pos]:
            min_pos = scan_pos
    rand_list[min_pos], rand_list[cur_pos] = rand_list[cur_pos], rand_list[min_pos] # commits the change

print(rand_list)

