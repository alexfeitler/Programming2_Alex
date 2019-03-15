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

# Insertion Sort
rand_list = [random.randrange(1, 100) for x in range(100)]
print(rand_list)

for key_pos in range(1, len(rand_list)):
    key_value = rand_list[key_pos]  # temporarily store the value
    scan_pos = key_pos - 1  # look to the dancer on left
    while (scan_pos >= 0) and (rand_list[scan_pos] > key_value):
        rand_list[scan_pos + 1] = rand_list[scan_pos]
        scan_pos -= 1

    # everything has shifted to make room for the key value
    rand_list[scan_pos + 1] = key_value
print(rand_list)

# Sorting in real life with Python
rand_list = [random.randrange(1, 100) for x in range(100)]
print(rand_list)
# Sort method (sorts in place; changes list directly)
rand_list.sort()
print(rand_list)

# Sorted function ( returns a sorted list)
rand_list = [random.randrange(1, 100) for x in range(100)]
print(rand_list)

rand_list2 = sorted(rand_list)  # capture the returned list
print(rand_list2)

# Optional Parameters
print("Hello", end="")  # end="" is and optional parameter that has a default value of "\n"
print("World")

def hello(name, time):
    print("Hello", name, "it is now", time)

hello("Karen", time="2:00 PM")
rand_list3 = sorted(rand_list)

# Lambda Function (anonymous function on a single line)
double_me = lambda x: 2 * x # Lambda parameter: return
print(double_me(10))


# Sorted function using Lambda function
# Optional key parameter is what you are using to sort the list
my_list = ["Abe", "Eva", "Zed", "Piper", "Len", "Jenny", "Kip"]
my_sort = sorted(my_list, key=lambda x: x.upper())
print(my_sort)

my_list.append("Alex")
my_sort = sorted(my_list, key=lambda x: len(x))
print(my_sort)

my_list = [["Abel", 8], ["Eva", 10], ["Zed", 11], ["Piper", 17], ["Len", 16], ["Jenny", 28], ["Kip", 80]]
my_sort = sorted(my_list, key=lambda x: x[1])
print(my_sort)

