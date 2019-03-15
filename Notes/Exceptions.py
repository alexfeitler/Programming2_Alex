# Exceptions

try:
    val = int(input("Enter a number: "))
except:
    print("You entered and invalid number")


# a better way to write it

done = False
while not done:
    try:
        val = int(input("Enter a number: "))
        done = True
    except:
        print("You entered and invalid number")

# Error Types
try:
    int("a")  # this line throws a value error
except:
    print("Value Error")

# Divide by zero
try:
    val = 3 / 0  # this produces a divide by zero error
except ZeroDivisionError:
    print("Zero Division Error")

# Input Output Error

try:
    my_file = open("my_file.txt")  # produces FileNotFoudError
except:
    print("File nto found")

# Catch Multiple Errors
try:
    y = 10 / 0
    int("A")
except Exception as e:
    print("Exception caught")
    print(e)

# Make MPG Calculator
done = False
while not done:
    try:
        miles = float(input("Miles Traveled: "))
        gallons = float(input("Gallons used: "))
        done = True
    except:
        print("You entered an invalid number")
try:
    print("Your MPG: {:.2f}".format(miles / gallons))
except:
    print("Your MPG is infinite. Your car must be electric")

# finally (always runs regardless of error or not)
try:
    my_file = open('my_file.txt', 'w')
    f = my_file.write("4-1 = 5")
except NameError:
    print("I/O error")
finally:
    my_file.close()